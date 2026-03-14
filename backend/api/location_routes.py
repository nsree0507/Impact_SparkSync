from fastapi import APIRouter
from backend.schemas.location_schema import LocationRequest
from backend.services.geofence_service import check_geofence
from backend.services.recommendation_service import get_recommendations
from backend.services.offer_service import generate_offer

router = APIRouter()


@router.post("/check-location")
def check_location(data: LocationRequest):
    """
    Check if customer is inside store geofence
    and generate personalized offers
    """

    customer_id = data.customer_id
    lat = data.latitude
    lon = data.longitude

    # Check geofence
    geofence_result = check_geofence(lat, lon)

    if not geofence_result["inside"]:
        return {
            "message": "User outside store area",
            "distance": geofence_result["distance"]
        }

    # Get product recommendations
    recommendations = get_recommendations(customer_id)

    offers = []

    # Generate offers for recommended products
    for product in recommendations:
        offer = generate_offer(customer_id, product)
        offers.append(offer)

    return {
        "message": "User inside store area",
        "distance": geofence_result["distance"],
        "offers": offers
    }