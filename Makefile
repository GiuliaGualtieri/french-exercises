.PHONY: format
.PHONY: format-check
.PHONY: lint
.PHONY: tests
.PHONY: build

# Format the code with black tool
format:
	black --fast french_exercises tests

# Check the formatting code with black
format-check:
	black --check french_exercises tests

# Check the code style
lint:
	ruff --fix french_exercises tests

# Launch the tests
test:
	pytest -v --doctest-modules tests

# Build the sdist and wheel packages
build:
	python -m build