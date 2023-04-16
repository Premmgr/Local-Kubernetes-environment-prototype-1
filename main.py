#!/usr/bin/env python3
import subprocess
import os
import platform
import sys
import shutil
import json
import time

"""Global varibales"""
minikube_path = 'minikube'
kubectl_path = 'kubectl'
linux_update=['apt','update']
kubectl_version="1.19.0"
user_bin_path = "/usr/local/bin"
scripts_path = 'scripts'
kubectl_bash_completion_script = "kubectl_bash_completion.sh"
scripts_path = "scripts"
minikube_bash_completion_script= "minikube_bash_completion.sh"
parent_dir = os.getcwd()
reset_path = lambda: os.chdir(parent_dir)
sleep = lambda seconds: time.sleep(seconds)
username = os.environ.get('SUDO_USER')
minikube_script="minikube_script.sh"

"""common function variables"""
def os_run(cmd):
    try:
        os.system(cmd)
    except ValueError as e:
        return e

def read_json(file_name):
    with open (file_name, 'r') as f:
        output_name = json.load(f)
        return output_name

def get_unix_val(file_name, key):
    with open (file_name, 'r') as f:
        output_name = json.load(f)
        data = []
        for i in output_name[f'{key}']:
            data.append(i)
        output = " ".join(data)
        return output

"""Docker class to perform specific docker action"""
class Docker:
    def install():
        subprocess.run(linux_update)
        os.chdir(scripts_path)
        os_run(cmd=f"./install-docker-ubuntu-server-22.04.sh {username}")
    reset_path()

"""Minikube function that downloads binary and place binary in bin dir"""
def minikube_install():
    try:
        os.mkdir(minikube_path)
    except FileExistsError as e:
        shutil.rmtree(f'{minikube_path}', ignore_errors=True)
        
    try:
        os.mkdir(minikube_path)
        os.chdir(minikube_path)
        subprocess.run(linux_update)
        subprocess.run(['curl','-LO', 'https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb'], check=True)
        subprocess.run(['dpkg', '-i', 'minikube_latest_amd64.deb'], check=True)
        shutil.rmtree(minikube_path, ignore_errors=True)
        subprocess.run(['minikube', 'version'])
        reset_path()
        shutil.rmtree(minikube_path, ignore_errors=True)
    except:
        pass

"""Execute minikube scripts from script dir"""
def minikube_exec(option=None):
    os.chdir(scripts_path)
    os.system(f'sudo -u {username} ./{minikube_script} {option}')
    reset_path()


"""Execute bash completion linux script """  
def bash_completion(name,script_name):
    err = f"Error while enabling {name} bash completion"
    try:
        os.chdir(scripts_path)
    except FileNotFoundError as e:
        print(f"{err}: {e}")
        return
    try:
        subprocess.run(f"./{script_name}", check=True)
        reset_path()
        print(f'✅  enabled {name} bash completion')
    except subprocess.CalledProcessError as e:
        print(f"{err}: {e}")


"""Download kubectl and installs binary"""
def kubectl_install(version):
    try:
        os.mkdir(kubectl_path)
    except FileExistsError:
        print(f'cleaning pre exiting {kubectl_path} path..')
        shutil.rmtree(f'{kubectl_path}', ignore_errors=True)
        os.mkdir(kubectl_path)
    try:
        os.chdir(kubectl_path)
        subprocess.run(linux_update)
        subprocess.run(['curl', '-LO', f'https://dl.k8s.io/release/v{version}/bin/linux/amd64/kubectl'], check=True)
        subprocess.run(['chmod','+x','kubectl'],check=True)
        subprocess.run(['mv', 'kubectl',f'{user_bin_path}'])
        reset_path()
        shutil.rmtree(kubectl_path, ignore_errors=True)
    except ValueError as e:
        print(f'error while installing kubctl: {e}')



# """Test"""

# """Check variables"""
# kubectl_check = subprocess.run(['which', 'kubectl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# minikube_check = subprocess.run(['which', 'minikube'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# docker_check = subprocess.run(['docker', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# """Auto installation"""
# if docker_check.returncode != 0:
#     Docker.install()
# else:
#     print(f'docker already installed, skipping...')

# if kubectl_check.returncode != 0:
#     print(kubectl_check.returncode)
#     print('Installing kubectl...')
#     kubectl_install(version=kubectl_version)
# else:
#     print(f'kubectl already installed, skipping...')


# if minikube_check.returncode != 0:
#     print('installing minikube')
#     minikube_install()
# else:
#     print(f'minikube already installed, skipping...')
    

# bash_completion(name="kubectl",script_name=kubectl_bash_completion_script)
# bash_completion(name="minikube",script_name=minikube_bash_completion_script)
