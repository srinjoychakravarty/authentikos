# Authentikos

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Authentikos is a python-based, tool-suite, that uses the power of Siacoin's SkyNet for distributed file storage and Byzantine Fault Tolerant BigChainDB as its distributed database. All Authentikos code is ledgered on Ethereum with the power of Solidity smart contracts.

### New Features

1. Command Line Interface to classify news articles into one of 6 labels with [FakerFact AI](https://www.fakerfact.org/about)
    * _faker_ai.py_
2. Upload and download images from Siacoin's distributed file storage network: SkyNet
    * _sia_upload_download.py_
3. Scrape EXIF metadata from images
    * _exif_scrape.py_ 

4. Write trust and familiarity ratings from .json text files to distributed databases 
    * _read_write_bigchain.py_

5. Reverse search and classify images using computer vision
    * _reverse_search.py_ 
6. Read/Write data about news agencies & articles from smart contracts
    * _solidity.py
    
7. Validate SSL certifications from registered news agency domains
    * _ssl_check.py_

> The overriding design goal for Authentikos'
> feature set is to make it as decentralized
> as possible. The idea is that a crowdsourced
> system that taps into the hive-mind, is able
> to collectively combat political disinformation
> by using the best in-class crytography,
> machine learning and artificial intelligence.

### Technology Stack

Authentikos uses a number of open source projects to work properly:
* [BigChainDB](https://www.bigchaindb.com/) - high-throughput, low-latency, immutable data storage with built-in asset support

* [Ethereum](https://ethereum.org/) - public, open-source, Blockchain-based distributed software platform

* [FakerFact](https://www.fakerfact.org/about) - Artificial intelligence tool trained on millions of blogs, science journals, opinion articles, hate speech, satire, narrative fiction & hyperpartisan news, to differentiate between credible information and manipulation

* [HERE WeGo Geocoder](https://developer.here.com/documentation/geocoder/dev_guide/topics/what-is.html) - RESTful API originally developed by Nokia for web mapping and navigation services

* [Python](https://www.python.org/) - interpreted, high-level, general-purpose programming language for code readability

* [Selenium](https://www.selenium.dev/) - webdriver to automate browser-based administration

* [Solidity](https://solidity.readthedocs.io/en/v0.6.7/) - statically typed, contract-oriented language that generates machine-level bytecode on the ethereum virtual machine to govern state transtions via smart contracts

* [SkyNet](https://siasky.net/) - decentralized file sharing and content distribution protocol

* [Yandex](https://yandex.com/images/) - search engine based on entire or fragments of images using computer vision algorithms

### Installation

Authentikos requires [Python 3.8.1](https://www.python.org/downloads/release/python-381/) to run.

##### For native Ubuntu / Debian hosts
_Skip to step 7_
##### For MacOS hosts
1. Install [VirtualBox 6.1.6](https://services.dartmouth.edu/TDClient/1806/Portal/KB/ArticleDet?ID=71778)

##### For Windows hosts
1. Install [VirtualBox 6.1.6](https://www.groovypost.com/howto/windows-10-install-virtualbox/)

##### For both MacOS & Windows hosts
2. Download [Zorin OS 15.2 Lite](https://zorinos.com/download/15/lite/)
3. Create a [Virtual Machine](https://linuxhint.com/install_zorin_os_virtualbox/)

4. Install Guest DKMS
    ```sh
    $ sudo apt-get install virtualbox-guest-dkms
    ```
5. Install VirtualBox [Guest Additions](https://helpdeskgeek.com/linux-tips/install-virtualbox-guest-additions-in-ubuntu/)

6. Reboot your Virtual Machine

##### For all Operating Systems  
###### (Debian-based Hosts or VMs i.e. _Zorin, Ubuntu, LXLE, Lubuntu etc._)
7. Open a new terminal window (Ctrl + Alt + T)

8. Install all required Linux kernel headers
    ```sh
    $ sudo apt install linux-headers-$(uname -r) -y
    ```
9.  Install packages needed for building general software
    ```sh
    $ sudo apt install build-essential -y
    ```
10. Download package information from all configured sources
    ```sh
    $ sudo apt-get update -y
    ```
11. Install available upgrades to all currently installed packages
    ```sh
    $ sudo apt-get upgrade -y
    ```
12. Intelligently resolves install / removal system package conflicts
    ```sh
    $ sudo apt-get dist-upgrade -y
    ```
13. Removes & purges orphaned packages no longer needed
    ```sh
    $ sudo apt-get autoremove --purge -y
    ```
14. Cleans obsolete debian packages
    ```sh
    $ sudo apt-get autoclean -y
    ```
15. Install common linux files required by Authentikos
    ```sh
    $ sudo apt install software-properties-common -y
    ```
16. Install git versioning tool for Github
    ```sh
    $ sudo apt install git -y
    ```
17. Required to download remote programs recursively    
    ```sh
    $ sudo apt install wget -y
    ```
18. Install curl to test connections to remote code repositories
    ```sh
    $ sudo apt install curl -y
    ```
19. Install support for client-server authentication with certificates
    ```sh
    $ sudo apt install apt-transport-https -y
    ```
20. Install certificate authorities to allow applications to check for SSL authencity
    ```sh
    $ sudo apt install ca-certificates -y
    ```
21. Compiles C code from source
    ```sh
    $ sudo apt-get install make -y
    ```
22. Install package manager for Python3
    ```sh
    $ sudo apt-get install python3-pip -y
    ```
23. Install google chrome to use as browser for automation
    ```sh
    $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    ```
    ```sh
    $ sudo apt install ./google-chrome-stable_current_amd64.deb -y
    ```
24. Install chromedriver to automate selenium scripts
    ```sh
    $ wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
    ```
    ```sh
    $ unzip chromedriver_linux64.zip
    ```
    ```sh
    $ sudo rm -rf chromedriver_linux64.zip
    ```
    ```sh
    $ sudo mv chromedriver /usr/bin/chromedriver
    ```
    ```sh
    $ sudo chown root:root /usr/bin/chromedriver
    ```
    ```sh
    $ sudo chmod +x /usr/bin/chromedriver
    ```
25. Install docker and docker-compose to run multi-container byzantine-fault tolerant, distributed database instance of BigChainDB; including its MongoDB base & Tendermint consensus layer
    ```sh
    $ sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    ```
    ```sh
    $ sudo chmod +x /usr/local/bin/docker-compose 
    ```
    ```sh
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```
    ```sh
    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
    ```
    ```sh
    $ sudo apt-cache policy docker-ce
    ```
    ```sh
    $ sudo apt install docker-ce -y 
    ```
26. Clone and run the BigChainDB repository
    ```sh
    $ sudo git clone https://github.com/bigchaindb/bigchaindb.git
    ```
    ```sh
    cd bigchaindb
     ```
     ```sh
     $ sudo make run
     ```
27. Open a new terminal window (Ctrl + Alt + T)

28. Install the ability to allow virtual python packages
   ```sh
   $ sueosdo apt-get install python3-venv -y
   ``` 
29. Clone the Authentikos repository
    ```sh
    $ git clone https://github.com/schaxz/authentikos.git
    ```
    ```sh
    $ cd authentikos
    ```
30. Create and activate Python Virtual Environment
    ```sh
    $ python3 -m venv env
    ```
    ```sh
    $ source env/bin/activate
    ```
31. Install all Authentikos python3 package dependencies
    ```sh
    (env) $ sudo pip3 install -r requirements.txt
    ```
