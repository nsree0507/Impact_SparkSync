from backend.services.inventory_service import inventory_based_discount
from backend.database.offer_repository import save_offer
from firebase.push_notification import send_notification


def generate_offer(customer_id: str, product: str):
    """
    Generate offer for customer based on recommendation
    """

    # Get inventory based discount
    inventory_offer = inventory_based_discount(product)

    # Create offer object
    offer = {
        "customer_id": customer_id,
        "product": product,
        "discount": inventory_offer["discount"],
        "stock_available": inventory_offer["stock"]
    }

    # Save offer to database
    save_offer(offer)

    # 🔔 Send push notification to customer
    try:
        title = "🎉 Special Store Offer!"
        message = f"{inventory_offer['discount']} OFF on {product}! Visit store now."

        send_notification(customer_id, title, message)

    except Exception as e:
        print("Notification failed:", str(e))

    return offer