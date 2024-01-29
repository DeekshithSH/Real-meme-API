from os import environ, cpu_count
from dotenv import load_dotenv

load_dotenv()

class Names(object):
    Device={
        "RMX1911(Old)": "📱 Realme 5(Old)",
        "RMX1925(Old)": "📱 Realme 5s(Old)",
        "RMX2030(Old)": "📱 Realme 5i(Old)",
        "r5x(Old)": "📱 Realme 5/5s/5i(Old)",
        "RMX1911": "📱 Realme 5",
        "RMX1925": "📱 Realme 5s",
        "RMX2030": "📱 Realme 5i",
        "R5X": "📱 Realme 5/5s/5i", 
        "Garnet": "📱 Poco X6/Redmi Note 13 Pro"
    }

    Type={
        "ROM":"📱💾 ROM",
        "Recovery":"📱🔧 Recovery",
        "Kernel":"📱🐧 Kernel"
    }
