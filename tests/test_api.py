import requests

BASE_URL = "http://127.0.0.1:8000"


def test_check_location():
    url = f"{BASE_URL}/check-location"

    data = {
        "customer_id": "C101",
        "latitude": 17.385,
        "longitude": 78.4867
    }

    response = requests.post(url, json=data)

    print("Status Code:", response.status_code)
    print("Response:", response.json())


def test_customer_offers():
    url = f"{BASE_URL}/customer/C101/offers"

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response:", response.json())


def test_loyalty_status():
    url = f"{BASE_URL}/customer/C101/loyalty"

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response:", response.json())


if __name__ == "__main__":
    test_check_location()
    test_customer_offers()
    test_loyalty_status()