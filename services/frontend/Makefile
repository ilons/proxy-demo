SHELL := /bin/bash

venv_path = .venv

DEFAULT_GOAL: help

.PHONY: \
	build \
	ensure-venv \
	help \
	run-dev \
	setup


build: ## Build service as Docker image using docker-compose
	docker-compose \
		-f docker-compose-dev.yml \
		build


ensure-venv: ## Create a local python environment if missing
	@if [[ ! -d "$(venv_path)" || ! -f "$(venv_path)/bin/activate" ]]; then \
		PIPENV_VENV_IN_PROJECT=true \
		python3.7 -m venv $(venv_path) \
	; fi


help: ## Print targets that have descriptions
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z_-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-25s\033[0m %s\n", $$1, $$2}'


run-dev: ## Run service locally
	docker-compose \
		-f docker-compose-dev.yml \
		up \
			frontend


setup: ensure-venv ## Make sure local environment are setup and requirements installed
	@echo "Installing pip requirements"
	@source $(venv_path)/bin/activate \
	&& pip install \
		--no-cache-dir \
		-r requirements.txt
