from backend.services.geofence_service import check_user_location


def test_geofence_inside():

    customer_id = "C101"
    latitude = 17.385
    longitude = 78.4867

    result = check_user_location(customer_id, latitude, longitude)

    print("Geofence Result:", result)


def test_geofence_outside():

    customer_id = "C101"
    latitude = 17.500
    longitude = 78.600

    result = check_user_location(customer_id, latitude, longitude)

    print("Geofence Result:", result)


if __name__ == "__main__":
    test_geofence_inside()
    test_geofence_outside()