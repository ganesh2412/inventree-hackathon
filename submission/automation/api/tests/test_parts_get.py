import pytest


def get_results(data):
    """Helper: handles both paginated {results:[...]} and plain list responses."""
    if isinstance(data, list):
        return data
    return data.get("results", [])


class TestPartsGet:
    """
    TC_API_001 to TC_API_010
    Tests for GET /api/part/ endpoint
    """

    def test_TC_API_001_list_all_parts(self, api_client, part_url):
        """TC_API_001: GET /api/part/ returns 200 and a list of parts."""
        response = api_client.get(part_url)
        assert response.status_code == 200
        data = response.json()
        assert "results" in data or isinstance(data, list)

    def test_TC_API_002_search_parts_by_keyword(self, api_client, part_url, created_part):
        """TC_API_002: Search filter returns matching parts."""
        name = created_part["name"]
        response = api_client.get(part_url, params={"search": name})
        assert response.status_code == 200
        results = get_results(response.json())
        assert any(p["name"] == name for p in results)

    def test_TC_API_003_filter_by_category(self, api_client, part_url, test_category_id, created_part):
        """TC_API_003: Filter by category returns only parts in that category."""
        response = api_client.get(part_url, params={"category": test_category_id})
        assert response.status_code == 200
        results = get_results(response.json())
        for part in results:
            assert part["category"] == test_category_id

    def test_TC_API_004_filter_active_parts(self, api_client, part_url):
        """TC_API_004: Filter active=true returns only active parts."""
        response = api_client.get(part_url, params={"active": True})
        assert response.status_code == 200
        results = get_results(response.json())
        for part in results:
            assert part["active"] is True

    def test_TC_API_005_filter_inactive_parts(self, api_client, part_url):
        """TC_API_005: Filter active=false returns only inactive parts."""
        response = api_client.get(part_url, params={"active": False})
        assert response.status_code == 200
        results = get_results(response.json())
        for part in results:
            assert part["active"] is False

    def test_TC_API_006_pagination_limit_offset(self, api_client, part_url):
        """TC_API_006: Pagination with limit=5 returns max 5 results."""
        response = api_client.get(part_url, params={"limit": 5, "offset": 0})
        assert response.status_code == 200
        results = get_results(response.json())
        assert len(results) <= 5

    def test_TC_API_007_filter_assembly_parts(self, api_client, part_url):
        """TC_API_007: Filter assembly=true returns only assembly parts."""
        response = api_client.get(part_url, params={"assembly": True})
        assert response.status_code == 200
        results = get_results(response.json())
        for part in results:
            assert part["assembly"] is True

    def test_TC_API_008_filter_purchaseable_parts(self, api_client, part_url):
        """TC_API_008: Filter purchaseable=true returns only purchaseable parts."""
        response = api_client.get(part_url, params={"purchaseable": True})
        assert response.status_code == 200
        results = get_results(response.json())
        for part in results:
            assert part["purchaseable"] is True

    def test_TC_API_009_no_auth_returns_401(self, base_url):
        """TC_API_009: Request without auth token returns 401."""
        import requests as req
        response = req.get(f"{base_url}/part/")
        assert response.status_code == 401

    def test_TC_API_010_invalid_filter_value_no_crash(self, api_client, part_url):
        """TC_API_010: Invalid filter value does not crash the server."""
        response = api_client.get(part_url, params={"active": "notabool"})
        assert response.status_code in [200, 400]


class TestPartGetById:
    """
    TC_API_024 to TC_API_028
    Tests for GET /api/part/{id}/
    """

    def test_TC_API_024_get_existing_part(self, api_client, part_url, created_part):
        """TC_API_024: Retrieve existing part by ID returns 200 and correct data."""
        part_id = created_part["pk"]
        response = api_client.get(f"{part_url}{part_id}/")
        assert response.status_code == 200
        data = response.json()
        assert data["pk"] == part_id

    def test_TC_API_025_get_nonexistent_part_returns_404(self, api_client, part_url):
        """TC_API_025: Retrieve non-existent part returns 404."""
        response = api_client.get(f"{part_url}9999999/")
        assert response.status_code == 404

    def test_TC_API_026_get_part_no_auth_returns_401(self, base_url, created_part):
        """TC_API_026: Retrieve part without auth returns 401."""
        import requests as req
        part_id = created_part["pk"]
        response = req.get(f"{base_url}/part/{part_id}/")
        assert response.status_code == 401

    def test_TC_API_027_get_part_with_string_id(self, api_client, part_url):
        """TC_API_027: Retrieve part with invalid string ID returns 404 or 400."""
        response = api_client.get(f"{part_url}abc/")
        assert response.status_code in [404, 400]

    def test_TC_API_028_response_contains_expected_fields(self, api_client, part_url, created_part):
        """TC_API_028: Part response includes all required fields."""
        part_id = created_part["pk"]
        response = api_client.get(f"{part_url}{part_id}/")
        assert response.status_code == 200
        data = response.json()
        expected_fields = ["pk", "name", "description", "category", "active",
                           "assembly", "virtual", "trackable", "purchaseable", "salable"]
        for field in expected_fields:
            assert field in data, f"Missing field: {field}"
