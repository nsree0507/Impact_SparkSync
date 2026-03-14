from backend.database.mongo_connection import get_database


db = get_database()

# Collections
customers_collection = db["customers"]
offers_collection = db["offers"]


def add_customer(customer_data: dict):
    """
    Insert new customer into database
    """

    result = customers_collection.insert_one(customer_data)

    return str(result.inserted_id)


def get_customer(customer_id: str):
    """
    Fetch customer details
    """

    customer = customers_collection.find_one(
        {"customer_id": customer_id},
        {"_id": 0}
    )

    return customer


def get_all_customers():
    """
    Fetch all customers
    """

    return list(customers_collection.find({}, {"_id": 0}))


def get_customer_offers(customer_id: str):
    """
    Fetch offers for a customer
    """

    offers = list(
        offers_collection.find(
            {"customer_id": customer_id},
            {"_id": 0}
        )
    )

    return offers