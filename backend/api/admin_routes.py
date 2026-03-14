from fastapi import APIRouter
from backend.database.mongo_connection import get_database

router = APIRouter()


# -----------------------------------
# View Transactions
# -----------------------------------
@router.get("/transactions")
def get_transactions():

    db = get_database()

    transactions = list(
        db["transactions"].find({}, {"_id": 0})
    )

    return {
        "total_transactions": len(transactions),
        "data": transactions
    }


# -----------------------------------
# Add Transaction
# -----------------------------------
@router.post("/add-transaction")
def add_transaction(transaction: dict):

    db = get_database()

    db["transactions"].insert_one(transaction)

    return {
        "message": "Transaction added successfully"
    }


# -----------------------------------
# Sales Summary
# -----------------------------------
@router.get("/sales-summary")
def sales_summary():

    db = get_database()

    pipeline = [
        {
            "$group": {
                "_id": None,
                "total_sales": {"$sum": "$Price"},
                "total_transactions": {"$sum": 1}
            }
        }
    ]

    result = list(db["transactions"].aggregate(pipeline))

    if not result:
        return {
            "total_sales": 0,
            "total_transactions": 0
        }

    return result[0]


# -----------------------------------
# Top Products
# -----------------------------------
@router.get("/top-products")
def top_products():

    db = get_database()

    pipeline = [
        {
            "$group": {
                "_id": "$Product",
                "total_sold": {"$sum": "$Quantity"}
            }
        },
        {"$sort": {"total_sold": -1}},
        {"$limit": 5}
    ]

    result = list(db["transactions"].aggregate(pipeline))

    return result


# -----------------------------------
# Customer Segments
# -----------------------------------
@router.get("/customer-segments")
def customer_segments():

    db = get_database()

    pipeline = [
        {
            "$group": {
                "_id": "$Customer_ID",
                "total_spent": {"$sum": "$Price"}
            }
        },
        {"$sort": {"total_spent": -1}}
    ]

    result = list(db["transactions"].aggregate(pipeline))

    return result