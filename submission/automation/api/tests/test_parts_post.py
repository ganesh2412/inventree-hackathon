import pytest


class TestPartsPost:
    """
    TC_API_011 to TC_API_023
    Tests for POST /api/part/ endpoint
    """

    def test_TC_API_011_create_part_required_fields(self, api_client, part_url, test_category_id):
        """TC_API_011: Create part with only required fields returns 201."""
        payload = {"name": "TC011 Part", "category": test_category_id}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "TC011 Part"
        # Cleanup
        api_client.delete(f"{part_url}{data['pk']}/")

    def test_TC_API_012_create_part_all_fields(self, api_client, part_url, test_category_id):
        """TC_API_012: Create part with all optional fields returns 201."""
        payload = {
            "name": "TC012 Full Part",
            "description": "Full test part",
            "category": test_category_id,
            "active": True,
            "assembly": False,
            "component": True,
            "purchaseable": True,
            "salable": False,
            "trackable": False,
            "virtual": False,
        }
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["description"] == "Full test part"
        assert data["purchaseable"] is True
        # Cleanup
        api_client.delete(f"{part_url}{data['pk']}/")

    def test_TC_API_013_create_part_missing_name_returns_400(self, api_client, part_url, test_category_id):
        """TC_API_013: Create part without name returns 400."""
        payload = {"category": test_category_id}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 400
        assert "name" in response.json()

    def test_TC_API_014_create_part_missing_category_returns_400(self, api_client, part_url):
        """TC_API_014: Create part without category returns 400."""
        payload = {"name": "No Category Part"}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 400

    def test_TC_API_015_create_part_invalid_category_returns_400(self, api_client, part_url):
        """TC_API_015: Create part with non-existent category ID returns 400."""
        payload = {"name": "Bad Category Part", "category": 9999999}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 400

    def test_TC_API_017_create_part_empty_name_returns_400(self, api_client, part_url, test_category_id):
        """TC_API_017: Create part with empty string name returns 400."""
        payload = {"name": "", "category": test_category_id}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 400

    def test_TC_API_018_create_part_no_auth_returns_401(self, base_url, test_category_id):
        """TC_API_018: Create part without auth token returns 401."""
        import requests as req
        payload = {"name": "Unauth Part", "category": test_category_id}
        response = req.post(
            f"{base_url}/part/",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 401

    def test_TC_API_019_create_virtual_part(self, api_client, part_url, test_category_id):
        """TC_API_019: Create part with virtual=True is created correctly."""
        payload = {"name": "TC019 Virtual Part", "category": test_category_id, "virtual": True}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["virtual"] is True
        api_client.delete(f"{part_url}{data['pk']}/")

    def test_TC_API_020_create_assembly_part(self, api_client, part_url, test_category_id):
        """TC_API_020: Create part with assembly=True is created correctly."""
        payload = {"name": "TC020 Assembly Part", "category": test_category_id, "assembly": True}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["assembly"] is True
        api_client.delete(f"{part_url}{data['pk']}/")

    def test_TC_API_021_create_trackable_part(self, api_client, part_url, test_category_id):
        """TC_API_021: Create part with trackable=True is created correctly."""
        payload = {"name": "TC021 Trackable Part", "category": test_category_id, "trackable": True}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["trackable"] is True
        api_client.delete(f"{part_url}{data['pk']}/")

    def test_TC_API_022_create_part_name_at_max_length(self, api_client, part_url, test_category_id):
        """TC_API_022: Create part with name at 100 characters succeeds."""
        long_name = "A" * 100
        payload = {"name": long_name, "category": test_category_id}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 201
        data = response.json()
        api_client.delete(f"{part_url}{data['pk']}/")

    def test_TC_API_023_create_part_name_exceeds_max_returns_400(self, api_client, part_url, test_category_id):
        """TC_API_023: Create part with name > 100 characters returns 400."""
        too_long_name = "A" * 200
        payload = {"name": too_long_name, "category": test_category_id}
        response = api_client.post(part_url, json=payload)
        assert response.status_code == 400
