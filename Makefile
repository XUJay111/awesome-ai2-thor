.PHONY: validate generate test check preview
PYTHON ?= python3

validate:
	$(PYTHON) scripts/validate_data.py

generate:
	$(PYTHON) scripts/generate_readme.py

test:
	$(PYTHON) -m unittest discover -s tests -v

check: validate test
	$(PYTHON) scripts/check_generated.py $(if $(AS_OF),--as-of $(AS_OF))

preview:
	$(PYTHON) -m http.server 8000 --bind 127.0.0.1 --directory docs
