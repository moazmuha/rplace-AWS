#!/bin/bash

#install docker(for AWS linux ami)
sudo yum update -y
sudo amazon-linux-extras install docker

#start docker service
sudo service docker start

#give ec2-user permissino to run docker without sudo
sudo usermod -a -G docker ec2-user

#run docker container
docker run -p 8080:8080 -p 8081:8081 moazmuha/rplace