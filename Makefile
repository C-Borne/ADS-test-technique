.PHONY: install
install: ## install packages and prepare environment
	poetry lock --check
	poetry install

.PHONY: requirements
requirements: ## run the code formatters
	poetry export -o requirements.txt --without-hashes --without-urls

