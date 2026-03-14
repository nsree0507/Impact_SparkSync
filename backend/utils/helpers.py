from datetime import datetime
import uuid


def generate_id(prefix: str):
    """
    Generate unique IDs like CUST_1234 or TXN_5678
    """
    unique = uuid.uuid4().hex[:6]
    return f"{prefix}_{unique}"


def current_timestamp():
    """
    Return current timestamp
    """
    return datetime.utcnow()


def format_offer(customer_id: str, product: str, discount: str, stock: int):
    """
    Standard offer format
    """
    return {
        "customer_id": customer_id,
        "product": product,
        "discount": discount,
        "stock_available": stock,
        "created_at": current_timestamp()
    }


def format_api_response(message: str, data=None):
    """
    Standard API response format
    """
    return {
        "message": message,
        "data": data,
        "timestamp": current_timestamp()
    }


def meters_to_km(distance_meters: float):
    """
    Convert meters to kilometers
    """
    return round(distance_meters / 1000, 2)