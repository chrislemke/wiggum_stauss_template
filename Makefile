.PHONY: setup

setup:
	@echo "==> Step 0: Installing system dependencies..."
	@OS=$$(uname); \
	if [ "$$OS" = "Darwin" ]; then \
		if brew bundle check --file=Brewfile > /dev/null 2>&1; then \
			echo "    All Homebrew dependencies already installed."; \
		else \
			echo "    Installing Homebrew dependencies from Brewfile..."; \
			brew bundle install --file=Brewfile; \
		fi; \
	else \
		echo "    Detected Linux — checking dependencies..."; \
		if ! command -v uv > /dev/null 2>&1; then \
			echo "    Installing uv..."; \
			curl -LsSf https://astral.sh/uv/install.sh | sh; \
		fi; \
		if ! command -v pre-commit > /dev/null 2>&1; then \
			echo "    Installing pre-commit..."; \
			pipx install pre-commit; \
		fi; \
		if ! command -v playwright > /dev/null 2>&1; then \
			echo "    Installing playwright..."; \
			pip install playwright && playwright install; \
		fi; \
	fi
	@echo ""
	@echo "==> Step 1: Project name"
	@read -p "Enter project name: " project_name; \
	if [ -z "$$project_name" ]; then \
		echo "Error: project name cannot be empty."; \
		exit 1; \
	fi; \
	\
	echo ""; \
	echo "==> Step 2: Renaming source package to src/$$project_name/..."; \
	mv src/project_name "src/$$project_name"; \
	\
	echo "==> Step 3: Creating tests skeleton..."; \
	mkdir -p tests; \
	touch tests/__init__.py; \
	touch tests/conftest.py; \
	\
	echo "==> Step 4: Replacing project_name with '$$project_name'..."; \
	OS=$$(uname); \
	if [ "$$OS" = "Darwin" ]; then \
		sed -i '' "s/project_name/$$project_name/g" "src/$$project_name/main.py" "src/$$project_name/__main__.py" pyproject.toml CLAUDE.md thoughts/shared/plan/IMPLEMENTATION_PLAN.md; \
	else \
		sed -i "s/project_name/$$project_name/g" "src/$$project_name/main.py" "src/$$project_name/__main__.py" pyproject.toml CLAUDE.md thoughts/shared/plan/IMPLEMENTATION_PLAN.md; \
	fi; \
	\
	echo "==> Step 5: Installing Python dependencies..."; \
	uv sync; \
	\
	echo "==> Step 6: Installing pre-commit hooks..."; \
	pre-commit install; \
	\
	echo ""; \
	echo "Setup complete! Project '$$project_name' is ready."

.PHONY: test

test:
	@exit_code=0; \
	r1=0; r2=0; r3=0; r4=0; r5=0; r6=0; r7=0; r8=0; \
	\
	echo "==> Step 1/8: Format"; \
	if uv run ruff format; then r1=0; echo "    ✓ format"; else r1=1; exit_code=1; echo "    ✗ format"; fi; \
	echo ""; \
	\
	echo "==> Step 2/8: Lint"; \
	if uv run ruff check . --fix; then r2=0; echo "    ✓ lint"; else r2=1; exit_code=1; echo "    ✗ lint"; fi; \
	echo ""; \
	\
	echo "==> Step 3/8: Typecheck"; \
	if uv run mypy --config-file=pyproject.toml src tests; then r3=0; echo "    ✓ typecheck"; else r3=1; exit_code=1; echo "    ✗ typecheck"; fi; \
	echo ""; \
	\
	echo "==> Step 4/8: Complexity"; \
	if uv run xenon --max-average=B --max-modules=B --max-absolute=B src; then r4=0; echo "    ✓ complexity"; else r4=1; exit_code=1; echo "    ✗ complexity"; fi; \
	echo ""; \
	\
	echo "==> Step 5/8: Security scan"; \
	if uv run bandit -c pyproject.toml -r .; then r5=0; echo "    ✓ security scan"; else r5=1; exit_code=1; echo "    ✗ security scan"; fi; \
	echo ""; \
	\
	echo "==> Step 6/8: Tests"; \
	if uv run pytest; then r6=0; echo "    ✓ tests"; else r6=1; exit_code=1; echo "    ✗ tests"; fi; \
	echo ""; \
	\
	echo "==> Step 7/8: Security audit"; \
	if uv run pip-audit; then r7=0; echo "    ✓ security audit"; else r7=1; exit_code=1; echo "    ✗ security audit"; fi; \
	echo ""; \
	\
	echo "==> Step 8/8: Mutation testing"; \
	if uv run mutmut run; then r8=0; echo "    ✓ mutation testing"; else r8=1; exit_code=1; echo "    ✗ mutation testing"; fi; \
	echo ""; \
	\
	echo "========================================"; \
	echo "  Summary"; \
	echo "========================================"; \
	if [ $$r1 -eq 0 ]; then echo "  PASS  Format";          else echo "  FAIL  Format";          fi; \
	if [ $$r2 -eq 0 ]; then echo "  PASS  Lint";            else echo "  FAIL  Lint";            fi; \
	if [ $$r3 -eq 0 ]; then echo "  PASS  Typecheck";       else echo "  FAIL  Typecheck";       fi; \
	if [ $$r4 -eq 0 ]; then echo "  PASS  Complexity";      else echo "  FAIL  Complexity";      fi; \
	if [ $$r5 -eq 0 ]; then echo "  PASS  Security scan";   else echo "  FAIL  Security scan";   fi; \
	if [ $$r6 -eq 0 ]; then echo "  PASS  Tests";           else echo "  FAIL  Tests";           fi; \
	if [ $$r7 -eq 0 ]; then echo "  PASS  Security audit";  else echo "  FAIL  Security audit";  fi; \
	if [ $$r8 -eq 0 ]; then echo "  PASS  Mutation testing"; else echo "  FAIL  Mutation testing"; fi; \
	echo "========================================"; \
	exit $$exit_code
