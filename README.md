# SmartShield: IoT-Based Emergency Alert Device for Women’s Safety

# 📖 Project Overview
SmartShield is an IoT-based personal safety device designed to assist women in alerting emergency contacts during unsafe situations. By pressing an emergency switch, the device immediately sends an alert email containing the user’s real-time location obtained through the LAN connection and a photo to a set of emergency contacts.

Built using a Raspberry Pi, this project incorporates an emergency switch to trigger the alert, a LAN-based location tracking feature, and a camera to capture images in real time.

# 🌟 Features
Emergency Switch Activation: A single press sends an email alert with the user’s location and a captured image.
LAN-Based Location Tracking: Captures the user’s current location using LAN.
Photo Attachment: Captures and sends an image to give emergency contacts more context.

# 🛠 Hardware and Software Requirements

# Hardware
Raspberry Pi (e.g., Raspberry Pi 3B+ or later)
Push Button Switch
Jumper Wires
USB Camera (compatible with Raspberry Pi)
Internet Connection (via LAN)

# Software
Operating System: Raspbian OS or similar
Programming Language: Python 3.7+
Required Libraries: smtplib, requests, dotenv (optional for environment variables)

# 📲 Usage Instructions
Power on your Raspberry Pi and ensure it’s connected to the LAN.
Press the emergency button to activate the alert.
The device will:
Capture the current location using LAN.
Capture an image via the USB camera.
Send an email with the location and image to the specified contacts.






