from backend.services.inventory_service import inventory_based_discount
from backend.database.offer_repository import save_offer


def generate_offer(customer_id: str, product: str):
    """
    Generate offer for customer based on recommendation
    """

    inventory_offer = inventory_based_discount(product)

    offer = {
        "customer_id": customer_id,
        "product": product,
        "discount": inventory_offer["discount"],
        "stock_available": inventory_offer["stock"]
    }

    # Save offer to database
    save_offer(offer)

    return offer