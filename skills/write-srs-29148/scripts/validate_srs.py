#!/usr/bin/env python3
"""Validate modular SRS directories produced by write-srs-29148."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REQ_ID_PATTERN = re.compile(r"\b(IR|FR|DR|NFR|CR)-\d{3}\b")

REQUIRED_SECTIONS = {
    "00": "Introduction",
    "01": "Product perspective",
    "02": "External interfaces",
    "03": "Functional requirements",
    "04": "Data requirements",
    "05": "Non-functional requirements",
    "06": "Constraints",
    "07": "Change control",
}

CATEGORY_PREFIX = {
    "IR": "02",
    "FR": "03",
    "DR": "04",
    "NFR": "05",
    "CR": "06",
}

REQUIRED_DEFINITIONS = [
    "SRS",
    "RTM",
    "MoSCoW",
    "IADT",
    "FR",
    "NFR",
    "DR",
    "IR",
    "CR",
]

REQUIRED_META_FIELDS = ("Priority:", "Verify:", "Release:")


@dataclass
class Finding:
    level: str
    message: str


def load_markdown_files(spec_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in spec_dir.iterdir()
        if path.is_file() and path.suffix.lower() == ".md"
    )


def validate_required_sections(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    names = [path.name for path in files]
    for prefix, title in REQUIRED_SECTIONS.items():
        if not any(name.startswith(prefix) for name in names):
            findings.append(Finding("error", f"Missing section {prefix} ({title})."))
    return findings


def validate_line_limits(files: list[Path], max_lines: int) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        line_count = len(path.read_text(encoding="utf-8").splitlines())
        if path.name.lower().startswith("rtm"):
            continue
        if line_count > max_lines:
            findings.append(
                Finding(
                    "error",
                    f"{path.name} has {line_count} lines (max {max_lines}); split this section.",
                )
            )
    return findings


def validate_definitions(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    intro = next((p for p in files if p.name.startswith("00")), None)
    if intro is None:
        return findings
    text = intro.read_text(encoding="utf-8")
    for term in REQUIRED_DEFINITIONS:
        if re.search(rf"\b{re.escape(term)}\b", text) is None:
            findings.append(
                Finding(
                    "error",
                    f"{intro.name} is missing required definition or acronym: {term}.",
                )
            )
    return findings


def validate_change_control(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    change_file = next((p for p in files if p.name.startswith("07")), None)
    if change_file is None:
        return findings
    text = change_file.read_text(encoding="utf-8")
    if "| Version | Date | Author | Changes |" not in text:
        findings.append(
            Finding(
                "error",
                f"{change_file.name} is missing the required version history table header.",
            )
        )
    if re.search(r"^\|\s*0\.1\s*\|", text, flags=re.MULTILINE) is None:
        findings.append(
            Finding(
                "warning",
                f"{change_file.name} does not include an initial 0.1 version row.",
            )
        )
    return findings


def validate_rtm(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    rtm_files = [p for p in files if p.name.lower().startswith("rtm")]
    for path in rtm_files:
        text = path.read_text(encoding="utf-8")
        required_header = "| Req ID | Requirement | Source/Need | Design Ref | Test Case | Status |"
        if required_header not in text:
            findings.append(
                Finding(
                    "warning",
                    f"{path.name} is missing the recommended RTM header row.",
                )
            )
    return findings


def validate_requirements(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    seen_ids: dict[str, tuple[Path, int]] = {}

    for path in files:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        id_lines: list[tuple[int, str]] = []

        for line_no, line in enumerate(lines, start=1):
            for match in REQ_ID_PATTERN.finditer(line):
                req = match.group(0)
                id_lines.append((line_no, req))
                if req in seen_ids:
                    original_path, original_line = seen_ids[req]
                    findings.append(
                        Finding(
                            "error",
                            (
                                f"Duplicate requirement ID {req} in {path.name}:{line_no}; "
                                f"already defined at {original_path.name}:{original_line}."
                            ),
                        )
                    )
                else:
                    seen_ids[req] = (path, line_no)

                category = req.split("-", maxsplit=1)[0]
                expected_prefix = CATEGORY_PREFIX[category]
                if not path.name.startswith(expected_prefix):
                    findings.append(
                        Finding(
                            "warning",
                            (
                                f"{req} appears in {path.name}; expected section prefix "
                                f"{expected_prefix} for {category} requirements."
                            ),
                        )
                    )

        # Validate requirement block quality for each ID occurrence.
        for index, (line_no, req_id) in enumerate(id_lines):
            start = line_no - 1
            end = len(lines)
            if index + 1 < len(id_lines):
                end = id_lines[index + 1][0] - 1
            block = "\n".join(lines[start:end])
            if re.search(r"\b(shall|should|may)\b", block, flags=re.IGNORECASE) is None:
                findings.append(
                    Finding(
                        "error",
                        f"{req_id} in {path.name}:{line_no} does not contain shall/should/may.",
                    )
                )
            for field in REQUIRED_META_FIELDS:
                if field not in block:
                    findings.append(
                        Finding(
                            "warning",
                            f"{req_id} in {path.name}:{line_no} is missing '{field}'.",
                        )
                    )

    # Ensure at least one requirement exists in each category file (02-06).
    for prefix in ("02", "03", "04", "05", "06"):
        section_files = [p for p in files if p.name.startswith(prefix)]
        if not section_files:
            continue
        if not any(REQ_ID_PATTERN.search(p.read_text(encoding="utf-8")) for p in section_files):
            findings.append(
                Finding(
                    "warning",
                    f"Section {prefix} has no requirement IDs detected.",
                )
            )

    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a modular SRS directory.")
    parser.add_argument("spec_dir", type=Path, help="Path to specs/<project-name>/ directory")
    parser.add_argument(
        "--max-lines",
        type=int,
        default=150,
        help="Maximum allowed lines per section file (default: 150, RTM excluded).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    spec_dir = args.spec_dir

    if not spec_dir.exists():
        print(f"ERROR: Directory does not exist: {spec_dir}")
        return 1
    if not spec_dir.is_dir():
        print(f"ERROR: Not a directory: {spec_dir}")
        return 1

    files = load_markdown_files(spec_dir)
    if not files:
        print(f"ERROR: No markdown files found in {spec_dir}")
        return 1

    findings: list[Finding] = []
    findings.extend(validate_required_sections(files))
    findings.extend(validate_line_limits(files, max_lines=args.max_lines))
    findings.extend(validate_definitions(files))
    findings.extend(validate_change_control(files))
    findings.extend(validate_rtm(files))
    findings.extend(validate_requirements(files))

    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]

    if errors:
        print("SRS validation failed.")
        for finding in errors:
            print(f"ERROR: {finding.message}")
        for finding in warnings:
            print(f"WARN: {finding.message}")
        return 1

    print("SRS validation passed.")
    for finding in warnings:
        print(f"WARN: {finding.message}")
    print(f"Checked {len(files)} markdown files in {spec_dir}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
