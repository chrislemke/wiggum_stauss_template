---
name: python-senior-practices
description: Senior-level Python 3.12+ engineering guidance for producing clean, typed, secure, and maintainable production code. Use when implementing, reviewing, refactoring, or debugging Python modules and services, especially for architecture decisions, data modeling, API boundaries, error handling, performance/concurrency choices, and security hardening.
---

# Python Senior Practices

Apply this skill to write or review production Python with explicit types, durable architecture, and strong operational safety.

## Quick Start

1. Clarify boundaries and failure modes first.
2. Type all public functions, class attributes, and return values.
3. Model structured data with immutable dataclasses by default.
4. Depend on protocols and injected collaborators, not concrete implementations.
5. Validate external input at boundaries and raise explicit exceptions.
6. Add or update tests for behavior and failure paths.

## Engineering Principles

Follow these defaults unless local project conventions explicitly override them:

- Prefer readability over cleverness.
- Prefer explicit behavior over hidden magic.
- Fail fast and fail loudly with specific exceptions.
- Prefer composition over inheritance.
- Make data immutable by default.

## Implementation Standards

### Type Hints

- Use built-in generics (`list[str]`, `dict[str, int]`), not legacy `typing.List` or `typing.Dict`.
- Use `X | Y` unions (`str | None`), not `Optional[str]`.
- Use PEP 695 syntax for generic aliases and functions where supported by project tooling.
- Accept abstract input types (`Sequence`, `Mapping`, `Iterable`) and return concrete output types (`list`, `dict`).

```python
from collections.abc import Iterable, Sequence

type Vector[T] = list[T]

def first[T](items: Sequence[T]) -> T:
    return items[0]

def transform(data: Iterable[int]) -> list[int]:
    return [value * 2 for value in data]
```

### Data Modeling

- Default to `@dataclass(frozen=True, slots=True)` for internal models.
- Use tuples for immutable sequences.
- Use Pydantic models at system boundaries (API payloads, config files, external data).

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Config:
    host: str
    port: int = 8080
    tags: tuple[str, ...] = ()
```

### Control Flow

- Use structural pattern matching when branch logic is shape-based and improves clarity.
- Use simple conditionals when matching adds noise.

```python
def handle(command: dict[str, object]) -> None:
    match command:
        case {"action": "create", "name": str(name)}:
            create(name)
        case {"action": "delete", "id": int(identifier)}:
            delete(identifier)
        case _:
            raise ValueError(f"Unknown command: {command}")
```

### Architecture and SOLID

- Give modules and classes a single reason to change.
- Extend behavior through protocols or new implementations, not large conditional branches.
- Keep contracts substitutable; do not narrow accepted inputs unexpectedly.
- Split interfaces by capability (for example, `ReadableStore` and `WritableStore`).
- Inject dependencies through constructors or function parameters.

```python
from typing import Protocol

class Repository(Protocol):
    def get(self, item_id: str) -> "Item": ...
    def save(self, item: "Item") -> None: ...

class UserService:
    def __init__(self, repo: Repository) -> None:
        self._repo = repo
```

### Error Handling

- Define domain-specific exception hierarchies.
- Catch only exceptions you can handle.
- Re-raise with `raise ... from exc` to preserve tracebacks.
- Log at the handling site.
- Let unexpected exceptions propagate.

```python
class AppError(Exception):
    """Base application exception."""

class NotFoundError(AppError):
    def __init__(self, entity: str, item_id: str) -> None:
        super().__init__(f"{entity} not found: {item_id}")
```

### Performance and Concurrency

- Profile before optimizing.
- Choose concurrency by workload:
  - Use `asyncio` for I/O-bound work.
  - Use `multiprocessing` for CPU-bound work.
  - Use `threading` for legacy blocking I/O when async is not practical.
- Prefer generators for single-pass consumption.
- Use efficient data structures (`set`, `deque`, `defaultdict`) based on access patterns.

Load [references/performance-async.md](references/performance-async.md) when designing async workflows, worker pools, or queue-based processing.

### Security Baseline

- Never use `eval`, `exec`, or untrusted `pickle` input.
- Parameterize SQL and query inputs.
- Validate all untrusted input at boundaries.
- Use secure password hashing (`bcrypt` or `argon2`).
- Keep secrets in environment variables or a vault, never in source.
- Generate tokens with `secrets`, not `random`.

Load [references/security-checklist.md](references/security-checklist.md) when handling authentication, sensitive data, external inputs, or dependency risk.

### Design Patterns

Apply patterns only when they remove real complexity, not preemptively.

Load [references/design-patterns.md](references/design-patterns.md) for selection guidance and Python-first idioms.

## Delivery Checklist

- Confirm naming and module boundaries are coherent.
- Confirm all public surfaces are typed.
- Confirm failure paths raise specific exceptions.
- Confirm tests cover happy path and key edge/failure paths.
- Confirm security-sensitive code follows checklist requirements.
