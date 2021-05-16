#!/bin/bash

#bootstrap script for AWS instances
#install docker(for AWS ubunutu AMI)
sudo su
apt update
Y | apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
Y | add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt install docker-ce docker-ce-cli containerd.io

#check that docker was installed
systemctl status docker

#make sure credentials are set
#run docker container(ensure security group is configured to allow this traffic)
docker run -p 80:8080 -p 8081:8081 huzaifam/rplace

#bootstrap script if created AMI
#!/bin/bash
sudo docker run -p 80:8080 -p 8081:8081 huzaifam/rplace