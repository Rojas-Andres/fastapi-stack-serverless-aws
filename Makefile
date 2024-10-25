.PHONY: help

.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.?## .$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build-sam:
	sam build --use-container --parameter-overrides Environment="local" GlobalTimeout="300"

local-sam: ## up d
	sam local start-api --parameter-overrides Environment="local" GlobalTimeout="300"

dev-check: ##Run all pre-commit hooks.
	@pre-commit run --all-files
