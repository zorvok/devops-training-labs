#!/bin/bash
set -e
sudo apt update
sudo apt install -y python3 python3-pip docker.io
pip3 install --user requests boto3
sudo usermod -aG docker $USER
echo '✅ Setup complete. Please log out and back in if Docker was just installed.'