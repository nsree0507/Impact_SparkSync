import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Store location configuration
STORE_LAT = 17.3850
STORE_LON = 78.4867

# Geofence radius in meters
GEOFENCE_RADIUS = 200

# MongoDB Atlas configuration
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "smart_retail_ai"

# Firebase configuration
FIREBASE_CREDENTIAL_PATH = "firebase/firebase-key.json"