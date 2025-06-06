import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

if BOT_TOKEN is None:
    print("Error: BOT_TOKEN not found in environment variables.")


if ADMIN_ID is None:
    print("Error: ADMIN_ID not found in environment variables.")
