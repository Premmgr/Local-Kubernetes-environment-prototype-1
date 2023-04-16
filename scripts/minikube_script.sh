#!/bin/bash
msg="😀  Local kubernetes environment is ready to use!"
if [[ $# -eq 0 ]]; then
	echo "available options [start, stop, purge, status]"
else
	case "$1" in
		"start")
			minikube status &> /dev/null && echo "😀  minikube already up and running"
			minikube status &> /dev/null || $(minikube start && echo "$msg") || echo "error while starting minikube"
		;;
		"stop")
			minikube stop
		;;
		"purge")
			minikube delete --purge
		;;
		"details")
			minikube status
		;;
	*)
		echo "available options [start, stop, purge, status]"
esac
fi
