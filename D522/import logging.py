import logging
from email.message import EmailMessage
import smtplib

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )
successes = 0
failures = 0

with open("devices.txt", "r") as file:
    devices = file.readlines()
    for device in devices:
        device = device.strip()
        if device == "bad_device":
            logging.error(f"{device} failed to process")
            failures += 1
        else:
            logging.info(f"{device} processed successfully")
            successes += 1
email_message = EmailMessage()
email_message.set_content(f"Processing completed. Successes: {successes}, Failures: {failures}")
email_message["Subject"] = "Device Processing Report"
email_message["From"] = "dlaroux@wgu.edu"
email_message["To"] = "recipient@wgu.edu"
with smtplib.SMTP("smtp.wgu.edu") as server:
    server.send_message(email_message)