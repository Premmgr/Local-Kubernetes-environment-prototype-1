#!/bin/bash
secret_name="$1"
username="$2"
password="$3"

# this script creates kubectl-cred with args
if [[ -z ${@} ]]; then
	echo "$0 <cred_name> <user_name> <password>"
else
	echo "$0 <cred_name> <user_name> <password>"
	kubectl create secret generic ${secret_name} --from-literal=username="${username}" --from-literal=password="${password}"
	echo -e "username:${username} \npassword: ${password}"
fi
