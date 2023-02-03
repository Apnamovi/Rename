import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26461352")

API_HASH = os.environ.get("API_HASH", "ab9cc32776ada8335852b50cd96bb8c6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6032337305:AAELEeju3NqZ1pQ2th5iMHEflAHmgJgiOm0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001647670460") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Jj2:Jj2@cluster0.8ij1dk5.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "50"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/884d04d7c61963dd0230a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5554564210').split()]

PORT = os.environ.get("PORT", "8080")
