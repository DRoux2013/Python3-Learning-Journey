import os
import requests

API_URL = "http://api.d522.wgu.internal:5000/api/tickets"
BEARER_TOKEN = os.getenv("HELPDESK_API_TOKEN")

if BEARER_TOKEN is None:
    print("Error: HELPDESK_API_TOKEN is not set")
else:
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if len(data) > 0:
                total_tickets = len(data)
                open_tickets = 0
                closed_tickets = 0
                high_priority_tickets = 0

                for ticket in data:
                    if ticket["status"] == "open":
                        open_tickets += 1
                    elif ticket["status"] == "closed":
                        closed_tickets += 1

                    if ticket["priority"] == "high":
                        high_priority_tickets += 1

                print(f"Total tickets: {total_tickets}")
                print(f"Open tickets: {open_tickets}")
                print(f"Closed tickets: {closed_tickets}")
                print(f"High-priority tickets: {high_priority_tickets}")
            else:
                print("No tickets found.")
        except ValueError:
            print("Error: Response is not valid JSON.")
    else:
        print(f"Request failed {response.status_code}")