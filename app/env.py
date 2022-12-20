import os


# get environment variables
path = os.getenv("API_DB_URL")
print("Environment", path)