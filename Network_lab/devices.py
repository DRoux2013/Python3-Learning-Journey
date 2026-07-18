import os

with open("devices.txt", "r") as file:
    lines = file.readlines()

updated_lines = []
for line in lines:
    device = line.strip()
    updated_line = device + " - READY FOR AUTOMATION"
    updated_lines.append(updated_line)

with open("devices.txt", "w") as file:
    for line in updated_lines:
        file.write(line + "\n")
os.makedirs("processed", exist_ok=True)
with open("processed/devices_processed.txt", "w") as file:
    for line in updated_lines:
        file.write(line + "\n")