#!/bin/bash
#run as su

apt-get update
wait
apt upgrade -y
wait
apt-get install python3
wait
apt-get install python3-opencv -y
wait
apt-get install cmake
wait
apt-get install gcc g++
wait
apt-get install python3-dev python3-numpy
wait
apt-get install libavcodec-dev libavformat-dev libswscale-dev
wait
apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
wait
apt-get install libgtk-3-dev
wait 
apt-get install libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev
wait
apt-get install git
wait
git clone https://github.com/opencv/opencv.git
wait
cd opencv
mkdir build
cd build
cmake ../
wait
make
wait
make install
wait
