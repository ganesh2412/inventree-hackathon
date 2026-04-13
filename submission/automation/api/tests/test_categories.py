import pytest
import uuid


@pytest.fixture
def cat_url(category_url):
    return category_url


class TestCategoriesGet:

    def test_TC_API_044_get_categories_returns_200(self, api_client, cat_url):
        """TC_API_044: GET /api/part/category/ returns 200."""
        r = api_client.get(cat_url)
        assert r.status_code == 200

    def test_TC_API_045_get_categories_returns_list(self, api_client, cat_url):
        """TC_API_045: GET /api/part/category/ returns a list."""
        r = api_client.get(cat_url)
        data = r.json()
        assert isinstance(data, list) or "results" in data

    def test_TC_API_046_category_has_required_fields(self, api_client, cat_url):
        """TC_API_046: Each category contains id, name fields."""
        r = api_client.get(cat_url)
        data = r.json()
        items = data.get("results", data) if isinstance(data, dict) else data
        if items:
            cat = items[0]
            assert "pk" in cat or "id" in cat
            assert "name" in cat

    def test_TC_API_047_get_category_no_auth_returns_401(self, cat_url):
        """TC_API_047: GET /api/part/category/ without auth returns 401."""
        import requests
        r = requests.get(cat_url)
        assert r.status_code == 401

    def test_TC_API_048_get_category_by_id(self, api_client, cat_url, test_category_id):
        """TC_API_048: GET /api/part/category/{id}/ returns 200 with correct id."""
        r = api_client.get(f"{cat_url}{test_category_id}/")
        assert r.status_code == 200
        assert r.json()["pk"] == test_category_id

    def test_TC_API_049_get_nonexistent_category_returns_404(self, api_client, cat_url):
        """TC_API_049: GET non-existent category returns 404."""
        r = api_client.get(f"{cat_url}999999/")
        assert r.status_code == 404

    def test_TC_API_050_category_response_is_json(self, api_client, cat_url):
        """TC_API_050: Response content-type is application/json."""
        r = api_client.get(cat_url)
        assert "application/json" in r.headers.get("Content-Type", "")


class TestCategoriesPost:

    def test_TC_API_051_create_category_returns_201(self, api_client, cat_url):
        """TC_API_051: POST creates category and returns 201."""
        name = f"AutoTestCat {uuid.uuid4().hex[:8]}"
        r = api_client.post(cat_url, json={"name": name, "description": "Test category"})
        assert r.status_code == 201
        cat_id = r.json()["pk"]
        api_client.delete(f"{cat_url}{cat_id}/")

    def test_TC_API_052_create_category_missing_name_returns_400(self, api_client, cat_url):
        """TC_API_052: POST without name returns 400."""
        r = api_client.post(cat_url, json={"description": "No Name"})
        assert r.status_code == 400

    def test_TC_API_053_create_category_with_parent(self, api_client, cat_url, test_category_id):
        """TC_API_053: POST creates child category under parent."""
        name = f"ChildCat {uuid.uuid4().hex[:8]}"
        r = api_client.post(cat_url, json={"name": name, "parent": test_category_id})
        assert r.status_code == 201
        assert r.json()["parent"] == test_category_id
        api_client.delete(f"{cat_url}{r.json()['pk']}/")

    def test_TC_API_054_create_category_response_has_pk(self, api_client, cat_url):
        """TC_API_054: POST response contains pk."""
        name = f"PkCat {uuid.uuid4().hex[:8]}"
        r = api_client.post(cat_url, json={"name": name})
        assert r.status_code == 201
        assert "pk" in r.json()
        api_client.delete(f"{cat_url}{r.json()['pk']}/")

    def test_TC_API_055_create_category_no_auth_returns_401(self, cat_url):
        """TC_API_055: POST without auth returns 401."""
        import requests
        name = f"UnAuthCat {uuid.uuid4().hex[:8]}"
        r = requests.post(cat_url, json={"name": name})
        assert r.status_code == 401

    def test_TC_API_056_create_duplicate_category_name(self, api_client, cat_url):
        """TC_API_056: POST with duplicate name returns 201 or 400."""
        name = f"DupCat {uuid.uuid4().hex[:8]}"
        r1 = api_client.post(cat_url, json={"name": name})
        assert r1.status_code == 201
        r2 = api_client.post(cat_url, json={"name": name})
        assert r2.status_code in [201, 400]
        api_client.delete(f"{cat_url}{r1.json()['pk']}/")
        if r2.status_code == 201:
            api_client.delete(f"{cat_url}{r2.json()['pk']}/")

    def test_TC_API_057_create_category_with_description(self, api_client, cat_url):
        """TC_API_057: POST with description stores it correctly."""
        name = f"DescCat {uuid.uuid4().hex[:8]}"
        r = api_client.post(cat_url, json={"name": name, "description": "A description"})
        assert r.status_code == 201
        assert r.json()["description"] == "A description"
        api_client.delete(f"{cat_url}{r.json()['pk']}/")

    def test_TC_API_058_patch_category_name(self, api_client, cat_url):
        """TC_API_058: PATCH updates category name."""
        name = f"PatchMe {uuid.uuid4().hex[:8]}"
        r = api_client.post(cat_url, json={"name": name})
        cat_id = r.json()["pk"]
        patched_name = f"Patched {uuid.uuid4().hex[:8]}"
        patch_r = api_client.patch(f"{cat_url}{cat_id}/", json={"name": patched_name})
        assert patch_r.status_code == 200
        assert patch_r.json()["name"] == patched_name
        api_client.delete(f"{cat_url}{cat_id}/")

    def test_TC_API_059_delete_category_returns_204(self, api_client, cat_url):
        """TC_API_059: DELETE category returns 204."""
        name = f"DeleteCat {uuid.uuid4().hex[:8]}"
        r = api_client.post(cat_url, json={"name": name})
        cat_id = r.json()["pk"]
        del_r = api_client.delete(f"{cat_url}{cat_id}/")
        assert del_r.status_code == 204

    def test_TC_API_060_delete_category_not_found(self, api_client, cat_url):
        """TC_API_060: DELETE non-existent category returns 404."""
        r = api_client.delete(f"{cat_url}999999/")
        assert r.status_code == 404
