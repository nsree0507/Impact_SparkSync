from backend.services.recommendation_service import get_recommendations


def test_recommendations():

    customer_id = "C101"

    recommendations = get_recommendations(customer_id)

    print("Recommended Products:", recommendations)


if __name__ == "__main__":
    test_recommendations()