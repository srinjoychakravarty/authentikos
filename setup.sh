#!/bin/bash
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt install linux-headers-$(uname -r) build-essential dkms -y
sudo apt install software-properties-common apt-transport-https wget -y
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo apt install code -y
sudo apt install curl -y
sudo apt install git -y
sudo apt-get install python3-pip -y
sudo pip3 install bigchaindb-driver
sudo pip3 install dataparser
sudo pip3 install flask
sudo pip3 install googletrans
sudo pip3 install inquirer
sudo pip3 install ipfshttpclient
sudo pip3 install pyOpenSSL
sudo pip3 install pywallet
sudo pip3 install selenium
sudo pip3 install siaskynet
sudo pip3 install tinydb
sudo pip3 install web3
sudo pip3 install wtforms

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo rm -rf chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver


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
wget https://dist.ipfs.io/go-ipfs/v0.4.23/go-ipfs_v0.4.23_linux-amd64.tar.gz
tar xvfz go-ipfs_v0.4.23_linux-amd64.tar.gz
rm go-ipfs_v0.4.23_linux-amd64.tar.gz
cd go-ipfs/
sudo ./install.sh
ipfs init
ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme
ipfs daemon