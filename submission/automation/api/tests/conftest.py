import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("INVENTREE_BASE_URL", "http://localhost")
API_TOKEN = os.getenv("INVENTREE_API_TOKEN", "inv-c4e3eb6724b125b6c2ca17a68204e9463b97d2e1-20260413")


@pytest.fixture(scope="session")
def api_client():
    """Returns a requests Session with auth headers pre-configured."""
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Token {API_TOKEN}",
        "Content-Type": "application/json",
    })
    return session


@pytest.fixture(scope="session")
def base_url():
    """Returns the InvenTree base API URL."""
    return f"{BASE_URL}/api"


@pytest.fixture(scope="session")
def part_url(base_url):
    """Returns the Parts endpoint URL."""
    return f"{base_url}/part/"


@pytest.fixture(scope="session")
def category_url(base_url):
    """Returns the Part Category endpoint URL."""
    return f"{base_url}/part/category/"


@pytest.fixture(scope="session")
def test_category_id(api_client, category_url):
    """Creates a test category and returns its ID. Cleaned up after session."""
    payload = {"name": "Hackathon Test Category", "description": "Auto-created for testing"}
    response = api_client.post(category_url, json=payload)
    assert response.status_code == 201, f"Failed to create test category: {response.text}"
    cat_id = response.json()["pk"]
    yield cat_id
    # Cleanup after tests
    api_client.delete(f"{category_url}{cat_id}/")


@pytest.fixture()
def created_part(api_client, part_url, test_category_id):
    """Creates a part for use in tests. Cleaned up after each test."""
    import uuid
    unique_name = f"Hackathon Test Part {uuid.uuid4().hex[:8]}"
    payload = {
        "name": unique_name,
        "description": "Auto-created for testing",
        "category": test_category_id,
        "active": True,
    }
    response = api_client.post(part_url, json=payload)
    assert response.status_code == 201, f"Failed to create test part: {response.text}"
    part = response.json()
    yield part
    # Cleanup
    api_client.delete(f"{part_url}{part['pk']}/")
