import os
import smtplib
import time
import requests
# import RPi.GPIO as GPIO
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime

# # GPIO setup for button (using GPIO 17)
# BUTTON_PIN = 17
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up to default HIGH

# Email configuration
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
TO_EMAIL = ""
SUBJECT = "Emergency Alert"

# Function to capture photo
def capture_photo():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    photo_filename = f"photo_{timestamp}.jpg"
    os.system(f"fswebcam -r 640x480 --jpeg 85 -D 1 {photo_filename}")
    return photo_filename

# Function to get location from IP
def get_ip_location():
    try:
        response = requests.get("http://ip-api.com/json")
        data = response.json()
        if data['status'] == 'success':
            latitude = data['lat']
            longitude = data['lon']
            city = data['city']
            country = data['country']
            # Generate Google Maps link with coordinates
            google_maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
            
            return (f"Lat: {latitude}, Lon: {longitude}, City: {city}, Country: {country}\n"
                    f"Google Maps: {google_maps_link}")
        else:
            return "Location not found"
    except Exception as e:
        return f"Error fetching location: {e}"

# Function to send email with the photo and location
def send_email(photo_filename, location):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    body = f"Emergency alert sent from Raspberry Pi.\nLocation: {location}"
    msg.attach(MIMEText(body, 'plain'))

    # Attach the photo
    with open(photo_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {photo_filename}")
        msg.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {TO_EMAIL}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function triggered by button press
def button_pressed_callback(channel=""):
    print("Press Enter to simulate button press...")
    input()  # Simulate the button press
    print("Button pressed! Capturing photo and sending alert...")

    # Capture photo
    photo_filename = capture_photo()
    print(f"Photo captured: {photo_filename}")

    # Get location
    location = get_ip_location()
    print(f"Location fetched: {location}")

    # Send email
    send_email(photo_filename, location)
    print("Email sent!")

# Set up event detection for the button
# GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed_callback, bouncetime=300)

# Main loop
print("Waiting for button press...")

try:
    button_pressed_callback()  # Simulate the button press for now
    while True:
        time.sleep(1)  # Keep the program running
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    print("Cleaning up...")
    # GPIO.cleanup()  # Clean up GPIO when done
