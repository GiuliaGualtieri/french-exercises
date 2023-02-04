.PHONY: format
.PHONY: format-check
.PHONY: lint
.PHONY: tests

# Format the code with black tool
format:
	black --fast french_exercises tests utils

# Check the formatting code with black
format-check:
	black --check french_exercises tests utils

# Check the code style
lint:
	ruff french_exercises tests utils

# Lunch the tests
test:
	pytest -v --doctest-modules tests