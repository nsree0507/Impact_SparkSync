import pandas as pd
from backend.models.recommender import recommend_products
from backend.database.mongo_connection import transactions_collection


def get_customer_purchase_history(customer_id):
    """
    Fetch purchase history from MongoDB
    """

    transactions = list(
        transactions_collection.find({"Customer_ID": customer_id})
    )

    if not transactions:
        return []

    products = [t["Product"] for t in transactions]

    return products


def get_recommendations(customer_id):
    """
    Generate product recommendations for a customer
    """

    # Fetch all transactions for model training
    transactions = list(transactions_collection.find())

    if not transactions:
        return []

    transactions_df = pd.DataFrame(transactions)

    purchased_products = get_customer_purchase_history(customer_id)

    if not purchased_products:
        return []

    recommendations = recommend_products(
        transactions_df,
        purchased_products
    )

    return recommendations