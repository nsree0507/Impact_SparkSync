from backend.database.mongo_connection import get_database


db = get_database()

# Transactions collection
transactions_collection = db["transactions"]


def add_transaction(transaction_data: dict):
    """
    Insert a new transaction into MongoDB
    """
    result = transactions_collection.insert_one(transaction_data)

    return str(result.inserted_id)


def get_all_transactions():
    """
    Fetch all transactions
    """
    return list(transactions_collection.find({}, {"_id": 0}))


def get_transactions_by_customer(customer_id: str):
    """
    Fetch transactions of a specific customer
    """
    return list(
        transactions_collection.find(
            {"Customer_ID": customer_id},
            {"_id": 0}
        )
    )


def get_sales_summary():
    """
    Calculate total sales amount
    """

    pipeline = [
        {
            "$group": {
                "_id": None,
                "total_sales": {"$sum": "$Price"},
                "total_transactions": {"$sum": 1}
            }
        }
    ]

    result = list(transactions_collection.aggregate(pipeline))

    if not result:
        return {
            "total_sales": 0,
            "total_transactions": 0
        }

    return result[0]


def get_top_products(limit: int = 5):
    """
    Return most purchased products
    """

    pipeline = [
        {
            "$group": {
                "_id": "$Product",
                "total_sales": {"$sum": "$Quantity"}
            }
        },
        {
            "$sort": {"total_sales": -1}
        },
        {
            "$limit": limit
        }
    ]

    result = list(transactions_collection.aggregate(pipeline))

    return result