import json

import requests

BASE_URL = "http://127.0.0.1:5000"


def print_result(title, response):
    """Print an API test result in a readable JSON format."""
    print(f"\n--- {title} ---")
    print(f"Status Code: {response.status_code}")
    print("JSON Response:")
    print(json.dumps(response.json(), indent=2))


def test_hello():
    """Test GET /hello."""
    response = requests.get(f"{BASE_URL}/hello", timeout=5)
    print_result("GET /hello", response)


def test_get_data():
    """Test GET /data."""
    response = requests.get(f"{BASE_URL}/data", timeout=5)
    print_result("GET /data", response)


def test_post_data():
    """Test POST /data."""
    payload = {
        "name": "Flask",
        "category": "Python Web Framework",
    }
    response = requests.post(
        f"{BASE_URL}/data",
        json=payload,
        timeout=5,
    )
    print_result("POST /data", response)


if __name__ == "__main__":
    test_hello()
    test_get_data()
    test_post_data()
