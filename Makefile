SHELL := /bin/bash

DEFAULT_GOAL: help

.PHONY: \
	build \
	help \
	run-dev \
	setup


build: ## Build images required to run demo
	docker-compose \
		build


help: ## Print targets that have descriptions
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z_-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-25s\033[0m %s\n", $$1, $$2}'

run-dev: ## Run service locally
	docker-compose \
		up \
		--force-recreate \
			api \
			frontend \
			site \
			proxy


setup: ## Run setup required for using repository locally
	@echo "nothing to do.."
