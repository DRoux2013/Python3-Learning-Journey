import os
API_KEY = os.getenv("API_KEY")
if API_KEY is None:
   print("Error: API_KEY is not set")
else:
   print("API key loaded successfully")