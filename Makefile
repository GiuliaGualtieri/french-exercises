.PHONY: format
.PHONY: format-check
.PHONY: lint
.PHONY: test
# .PHONY: docs
.PHONY: changelog
.PHONY: patch
.PHONY: minor
.PHONY: major

# Format the code with black tool
format:
	black --fast src tests utils

# Check the formatting code with black
format-check:
	black --check src tests utils

# Check the code style
lint:
	pylint src tests utils

# Lunch the tests
test:
	pytest -v --doctest-modules tests

# Update the changelog file
changelog:
	gitchangelog > CHANGELOG.md
	git add CHANGELOG.md
	git commit -m "chg: Update changelog"

# create the docs
docs:
	python -m utils.autodocs src

# release a patch
patch:
	python -m utils.release patch

# release a minor version
minor:
	python -m utils.release minor

# release a major version
major:
	python -m utils.release major