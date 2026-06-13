import os
import sys
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("ERROR: GROQ_API_KEY not found in .env file!")
    print("Please add your API key to .env")
    sys.exit(1)

# System Configuration
JARVIS_NAME = os.getenv("JARVIS_NAME", "JARVIS")
USER_NAME = os.getenv("USER_NAME", "Sir")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Database
DB_PATH = "jarvis_data.db"

# Voice Configuration
VOICE_RATE = 150
VOICE_VOLUME = 1.0
SPEECH_LANGUAGE = "en"

# Timeouts (IMPORTANT - Increase these to let you finish speaking)
SPEECH_TIMEOUT = 30  # Increased from 10 to 30 seconds - gives you more time to speak
PHRASE_TIME_LIMIT = 10  # Max time to wait for silence before processing

print(f"✓ Config loaded - API Key: {GROQ_API_KEY[:10]}...")
print(f"✓ Speech Language: {SPEECH_LANGUAGE}")
print(f"✓ Speech Timeout: {SPEECH_TIMEOUT}s")