.PHONY: validate generate check

validate:
	python scripts/validate_data.py

generate:
	python scripts/generate_readme.py

check: validate generate
	git diff --exit-code README.md
