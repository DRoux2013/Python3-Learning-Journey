import logging

logging.basicConfig(
    filename='automation.log'
    level=logging.INFO
    format="%(asctime)s - %(levelname)s - %(message)s"
)
with open('devices.txt', 'r') as file:
    devices = file.readlines()