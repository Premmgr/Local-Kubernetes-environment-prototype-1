#!/bin/bash
REPO=""
DOCKER_EDITION="docker-ce"
USER="$1"

# install docker if not isntalled
function install_docker(){
	set -eof
	apt update -y
	apt install docker-ce docker-compose -y
	if [[ ! $1 ]]; then
		echo "no user added to docker group"
	else
		echo "adding $1 to docker group"
		usermod -aG docker $1
	fi
	systemctl restart docker
}

function repo_setup(){
	apt update
	echo "installing common packages for ${DOCKER_EDITION}"
	apt install apt-transport-https ca-certificates curl software-properties-common -y
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
	echo "adding apt repository"
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	apt-cache policy "${DOCKER_EDITION}"

}

# installation

if [[ ! "$(id -u)" = "0" ]]; then
	echo "try with sudo $0"
else
	repo_setup
	install_docker $USER
fi	
