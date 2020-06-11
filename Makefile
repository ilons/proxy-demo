SHELL := /bin/bash

DEFAULT_GOAL: help

.PHONY: \
	build \
	clean \
	help \
	run \
	setup


build: ## Build images required to run demo
	docker-compose \
		build


clean: ## Clean up docker resources created
	docker-compose \
		down \
		--remove-orphans \
		--volumes


help: ## Print targets that have descriptions
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z_-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-25s\033[0m %s\n", $$1, $$2}'


run: ## Run service locally
	docker-compose \
		up \
		--force-recreate \
			api \
			frontend \
			site \
			proxy


setup: ## Run setup required for using repository locally
	$(MAKE) -C services/api $@
