"""Practice: for loops over a list."""

DEVICES = ["router1", "switch1", "firewall1", "accesspoint1"]

def main():
    for device in DEVICES:
        print(f"Checking {device}")
        
if __name__== "__main__":
    main()