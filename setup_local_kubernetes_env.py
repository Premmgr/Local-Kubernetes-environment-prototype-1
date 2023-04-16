#!/usr/bin/env python3
import os, time
from main import Docker
from main import kubectl_install, minikube_install, kubectl_version, kubectl_bash_completion_script, minikube_bash_completion_script, bash_completion
from main import minikube_exec
import argparse

username = os.environ.get('SUDO_USER')
msg="😀  Local kubernetes environment is ready to use!"

slp=time.sleep(0.3)

# Check if the necessary dependencies are installed
kubectl_check = os.system('which kubectl > /dev/null')
minikube_check = os.system('which minikube > /dev/null')
docker_check = os.system('docker info > /dev/null')
minikube_status = os.system('minikube status > /dev/null')

"""Auto installation"""
slp
if docker_check != 0:
    Docker.install()
else:
    print(f'🐳  docker already installed, skipping...')
slp
if kubectl_check != 0:
    print('✅  Installing kubectl...')
    kubectl_install(version=kubectl_version)
else:
    print(f'✅  kubectl already installed, skipping...')

slp
if minikube_check != 0:
    print('✅  installing minikube')
    minikube_install()
else:
    print(f'✅  minikube already installed, skipping...')
    
# print(os.getcwd())
bash_completion(name="kubectl",script_name=kubectl_bash_completion_script)
bash_completion(name="minikube",script_name=minikube_bash_completion_script)

"""To prevent security risks default minikube runs with nonroot user (sudo user)"""
if username == None:
    username = 'root'

minikube_exec(option='start')
