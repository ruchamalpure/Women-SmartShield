#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install required packages
echo "Installing required packages..."
sudo apt-get install -y fswebcam python3-smtplib python3-requests python3-rpi.gpio

# Confirmation message
echo "Installation complete!"
