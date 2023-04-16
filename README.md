# Local kubernetes env setup

## Description
This is experimental kubernetes local environment setup (only tested on Ubuntu 22.04)

--------------------------------------------------
What this project provides
- Prepare the local kubernetes environment
- Install docker on Ubuntu 22.04 LTS (Desktop/Server) and append current user to docker group
- Install minikube enable bash-completion for minikube (if not installed)
- install kubectl and enable bash-completion for kubectl (if not installed)

--------------------------------------------------

## Table of Contents (Optional)

- [Installation](#installation)
- [Usage](#usage)

--------------------------------------------------

## Installation

What are the steps required to install your project? Provide a step-by-step description of how to get the development environment running.

## Usage

- Setup local kubernetes env as a root user  
```$ cd local_kubernetes_env```  
```$ chmod +x ./setup_local_kubernetes_env.sh```  
```$ ./setup_local_kubernetes_env.sh```  

- Setup local kubernetes env as a sudo user  
```$ cd local_kubernetes_env```  
```$ sudo chmod +x ./setup_local_kubernetes_env.sh```  
```$ sudo ./setup_local_kubernetes_env.sh```  

