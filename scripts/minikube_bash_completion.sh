#!/bin/bash

if [[ ! "$(id -u)" = "0" ]]; then
        echo "required root permission $0"
	exit 1
else
	# Check if minit is installed
    if ! command -v minikube &> /dev/null
	then
    		echo "minikube not found. Please install kubectl."
    		exit 1
	else
		set -e
		# Enable bash completion for minikube
		minikube completion bash > /etc/bash_completion.d/minikube
		source /etc/bash_completion.d/minikube
		exit 0
	fi
fi

