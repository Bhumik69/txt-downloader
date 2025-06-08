import os

API_ID = API_ID =  21667419

API_HASH = os.environ.get("API_HASH", "841be499a8c26b7e6156d4251fe5fdc3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7863263352:AAFiwULvpDNtworhwCAMZxeDAPqKaR6WNto")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7919334195))

LOG = -1002159628443,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[6938835589]
    for x in (os.environ.get("ADMINS", "6938835589").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
