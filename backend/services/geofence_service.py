from geopy.distance import geodesic
from backend.utils.config import STORE_LAT, STORE_LON, GEOFENCE_RADIUS


def check_geofence(user_lat, user_lon):
    """
    Check if user entered store geofence
    """

    store_location = (STORE_LAT, STORE_LON)
    user_location = (user_lat, user_lon)

    distance = geodesic(store_location, user_location).meters

    if distance <= GEOFENCE_RADIUS:
        return {
            "inside": True,
            "distance": round(distance, 2)
        }

    return {
        "inside": False,
        "distance": round(distance, 2)
    }