#!/bin/bash

sudo apt install linux-headers-$(uname -r) build-essential dkms -y
sudo apt install software-properties-common apt-transport-https wget -y
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo apt-get install python3-pip -y
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt install code -y
sudo apt install git -y
sudo pip3 install pyOpenSSL
sudo pip3 install tinydb
sudo pip3 install sudo pip3 install dataparser
sudo pip3 install bigchaindb-driver
sudo apt install curl -y
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
sudo apt-cache policy docker-ce
sudo apt install docker-ce -y 
sudo apt-get install make -y
sudo git clone https://github.com/bigchaindb/bigchaindb.git
cd bigchaindb
sudo make run
sudo git clone https://github.com/schaxz/hyperpartisan_news_index.git
