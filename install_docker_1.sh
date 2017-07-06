#!bin/bash 

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common


echo "Adding Docker’s official GPG key: "
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -



echo "updating"

sudo apt-get update


echo "install ce"

sudo apt-get install docker-ce