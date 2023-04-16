#!/bin/bash

if [[ ! "$(id -u)" = "0" ]]; then
        echo "required root permission $0"
	exit 1
else
	# Check if kubectl is installed
        if ! command -v kubectl &> /dev/null
	then
    		echo "kubectl not found. Please install kubectl."
    		exit 1
	else
		# Enable bash completion for kubectl
		kubectl completion bash > /etc/bash_completion.d/kubectl
        	source /etc/bash_completion.d/kubectl
			exit 0
	fi
fi
