from backend.database.mongo_connection import get_database
from firebase.push_notification import send_push_notification

# Get database instance
db = get_database()

# Device token collection
device_tokens_collection = db["device_tokens"]


def get_device_token(customer_id: str):
    """
    Fetch device token for a customer
    """

    token_data = device_tokens_collection.find_one(
        {"customer_id": customer_id}
    )

    if not token_data:
        return None

    return token_data.get("device_token")


def send_customer_notification(customer_id: str, title: str, message: str):
    """
    Send push notification to a specific customer
    """

    token = get_device_token(customer_id)

    if not token:
        return {
            "status": "failed",
            "message": "Device token not found"
        }

    try:
        response = send_push_notification(token, title, message)

        return {
            "status": "success",
            "firebase_response": str(response)
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }