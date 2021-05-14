#!/bin/bash

#bootstrap script for AWS instances
#install docker(for AWS ubunutu AMI)
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt install docker-ce docker-ce-cli containerd.io

#check that docker was installed
sudo systemctl status docker

#run docker container(ensure security group is configured to allow this traffic)
sudo docker run -p 80:8080 -p 8081:8081 moazmuha/rplace