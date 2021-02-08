#! /bin/bash

# Install wget if it's not already installed
sudo apt install -y wget 

# Downlod the dataset
wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

# Create Dicrectory if it already does not exist
DIRNAME="data"
if [ -d $DIRNAME ]
then
    echo "Directory: $DIRNAME Already Exists"
else
    echo "Directory Does not exit. Creating Directory: $DIRNAME"
    mkdir $DIRNAME
fi

# Untar the file & Remove the Compressed File
tar -zxvf cifar-10-python.tar.gz -C $DIRNAME
rm -f cifar-10-python.tar.gz