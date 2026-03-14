from backend.database.mongo_connection import get_database

# Get database instance
db = get_database()

# Access transactions collection
transactions_collection = db["transactions"]


def calculate_loyalty_score(customer_id: str):
    """
    Calculate loyalty score based on spending and purchases
    """

    transactions = list(
        transactions_collection.find({"Customer_ID": customer_id})
    )

    if not transactions:
        return {
            "score": 0,
            "level": "New Customer"
        }

    total_spending = sum(t.get("Price", 0) for t in transactions)
    purchase_count = len(transactions)

    score = total_spending + (purchase_count * 10)

    if score > 1500:
        level = "VIP"
    elif score > 500:
        level = "Regular"
    else:
        level = "New Customer"

    return {
        "score": score,
        "level": level
    }