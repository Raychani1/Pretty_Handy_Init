#!/bin/bash

function pretty_handy_init() {
	GIT_ENV="<PATH-TO-PROJECT>/example_env/example_git.env"
	DOCKERHUB_ENV="<PATH-TO-PROJECT>/example_env/example_dockerhub.env"

	if [[ -z "$DOCKERHUB_ENV" ]]; then
		docker run --rm -it --name init_container -v "$(pwd)":/app/init_dir --env-file "$GIT_ENV" rajcsanyiladislavit/pretty_handy_init:latest "$@"
	else
		docker run --rm -it --name init_container -v "$(pwd)":/app/init_dir --env-file "$GIT_ENV" --env-file "$DOCKERHUB_ENV" rajcsanyiladislavit/pretty_handy_init:latest "$@"
	fi
}
