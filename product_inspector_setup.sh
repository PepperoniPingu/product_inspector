#! /bin/bash

echo "Fedora or Debian based distro? f/d"
read distro
echo "Shell? Bash or ZSH?"
read shell


if [ "${distro,,}" == "f" ]; then   # Fedora install
    
    sudo dnf install git pip conda
    
elif [ "${distro,,}" == "d" ]; then # Debian install
    
    sudo apt-get install git pip conda

else
    echo "Error: Answer 'f' or 'd"
fi

# Setup Python installation
conda init "${shell,,}"
conda create -n anomalib_env python=3.10
conda activate anomalib_env
git clone https://github.com/openvinotoolkit/anomalib.git
cd anomalib
pip install -e .
cd ..

# Download test datasets
mkdir datasets
cd datasets
wget -O mvtech_anomaly_detection.tar.gz https://www.mydrive.ch/shares/38536/3830184030e49fe74747669442f0f282/download/420938113-1629952094
mkdir mvtech_anomaly_detection
cd mvtech_anomaly_detection
echo "Extracting test dataset..."
tar -xf ../mvtech_anomaly_detection.tar.gz -C
rm mvtech_anomaly_detection.tar.gz
cd ../..

echo "Done"