from backend.database.mongo_connection import get_database


def check_inventory(product_name: str):
    """
    Check inventory level of a product
    """

    db = get_database()
    inventory_collection = db["inventory"]

    product = inventory_collection.find_one({"product": product_name})

    if not product:
        return {
            "product": product_name,
            "stock": 0
        }

    return product


def inventory_based_discount(product_name: str):
    """
    Generate discount based on stock level
    """

    inventory = check_inventory(product_name)

    stock = inventory.get("stock", 0)

    if stock > 200:
        discount = "30%"
    elif stock > 100:
        discount = "20%"
    elif stock > 50:
        discount = "10%"
    else:
        discount = "5%"

    return {
        "product": product_name,
        "stock": stock,
        "discount": discount
    }