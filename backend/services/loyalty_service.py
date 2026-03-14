from backend.database.mongo_connection import transactions_collection


def calculate_loyalty_score(customer_id):
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

    total_spending = sum(t["Price"] for t in transactions)
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