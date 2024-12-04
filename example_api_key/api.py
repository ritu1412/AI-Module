import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("DESIGNTK_API_KEY")

# Use the API key in your code
print(api_key)