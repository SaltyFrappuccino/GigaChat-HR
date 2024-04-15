import os

from dotenv import load_dotenv

load_dotenv()

scope = os.getenv("SCOPE")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
auth_data = os.getenv("AUTH_DATA")
debug = os.getenv("DEBUG")
if debug == "True":
    debug = True
else:
    debug = False
