from os import environ, cpu_count
from dotenv import load_dotenv

load_dotenv()

class Var(object):
   API_ID:int = int(environ.get("API_ID"))
   API_HASH:str = str(environ.get("API_HASH"))
   DATABASE_URL:int = str(environ.get('DATABASE_URL'))
   BOT_TOKEN = str(environ.get("BOT_TOKEN"))

   PORT = int(environ.get("PORT", 8080))
   BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
   HAS_SSL = environ.get("HAS_SSL", False)
   HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
   NO_PORT = environ.get("NO_PORT", False)
   NO_PORT = True if str(NO_PORT).lower() == "true" else False
   FQDN = str(environ.get("FQDN", BIND_ADDRESS))
   URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT))
