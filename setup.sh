#!/bin/bash

sudo chmod +x apt_bdb.sh
sudo chmod +x venv_pip.sh
echo "Installing all python3 prerequisites and bigchaindb for Authentikos..."
x-terminal-emulator -e bash ./apt_bdb.sh
return
echo "Installing required pip3 packages for Authentikos..."
x-terminal-emulator -e bash ./venv_pip.sh 
