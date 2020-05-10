#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get autoremove --purge -y
sudo apt-get autoclean -y
sudo apt install linux-headers-$(uname -r) -y
sudo apt install build-essential -y
sudo apt install software-properties-common -y
sudo apt install git -y
sudo apt install wget -y
sudo apt install curl -y
sudo apt install apt-transport-https -y
sudo apt install ca-certificates -y
sudo apt-get install make -y
sudo apt-get install python3-venv -y
sudo apt-get install python3-pip -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo rm -rf chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt-cache policy docker-ce
sudo apt install docker-ce -y
sudo apt install rng-tools -y
sudo apt-get install haveged -y
sudo update-rc.d haveged defaults
cd ..
sudo git clone https://github.com/bigchaindb/bigchaindb.git
cd bigchaindb
sudo make run &
