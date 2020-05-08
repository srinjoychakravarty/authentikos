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

8. Install git versioning tool for Github
    ```sh
    $ sudo apt install git -y
    ```
9. Clone this Authentikos repository
   ```sh
   $ git clone https://github.com/srinjoychakravarty/authentikos.git
   ```
10. Move into the Authentikos repository and make the setup script executable
   ```sh
   $ cd authentikos
   ```
   ```sh
   $ sudo chmod +x setup.sh
   ```

8. Run the setup to install all the software prerequisites for Authentikos
    ```sh
    $ sudo ./setup.sh
    ```
