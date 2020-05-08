#!/bin/bash
echo "This script is about to run another script."
sudo chmod +x apt_bdb.sh
sudo chmod +x venv_pip.sh
echo "This script has just run another script."
gnome-terminal -e sh ./apt_bdb.sh
gnome-terminal -e sh ./venv_pip.sh 
