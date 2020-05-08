#!/bin/bash

sudo apt-get update && sudo apt-get upgrade

sudo pip3 install opencv-contrib-python-headless==3.4.6.27
sudo apt-get install -y libcblas-dev
sudo apt-get install -y libhdf5-dev
sudo apt-get install -y libhdf5-serial-dev
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libjasper-dev
sudo apt-get install -y libqtgui4
sudo apt-get install -y libqt4-test

python3 -c "import cv2"