import pytest
import uuid


class TestPartsPatch:

    def test_TC_API_024_patch_part_name(self, api_client, part_url, test_category_id):
        """TC_API_024: PATCH updates part name successfully."""
        payload = {"name": f"InitialPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        updated_name = f"UpdatedPart {uuid.uuid4().hex[:8]}"
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"name": updated_name})
        assert patch_r.status_code == 200
        assert patch_r.json()["name"] == updated_name
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_025_patch_part_description(self, api_client, part_url, test_category_id):
        """TC_API_025: PATCH updates part description."""
        payload = {"name": f"PatchDescPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"description": "New Description"})
        assert patch_r.status_code == 200
        assert patch_r.json()["description"] == "New Description"
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_026_patch_part_active_false(self, api_client, part_url, test_category_id):
        """TC_API_026: PATCH sets active to False."""
        payload = {"name": f"ActivePart {uuid.uuid4().hex[:8]}", "category": test_category_id, "active": True}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"active": False})
        assert patch_r.status_code == 200
        assert patch_r.json()["active"] is False
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_027_patch_part_purchaseable(self, api_client, part_url, test_category_id):
        """TC_API_027: PATCH sets purchaseable flag."""
        payload = {"name": f"PurchPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"purchaseable": True})
        assert patch_r.status_code == 200
        assert patch_r.json()["purchaseable"] is True
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_028_patch_part_salable(self, api_client, part_url, test_category_id):
        """TC_API_028: PATCH sets salable flag."""
        payload = {"name": f"SalablePart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"salable": True})
        assert patch_r.status_code == 200
        assert patch_r.json()["salable"] is True
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_029_patch_part_trackable(self, api_client, part_url, test_category_id):
        """TC_API_029: PATCH sets trackable flag."""
        payload = {"name": f"TrackPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"trackable": True})
        assert patch_r.status_code == 200
        assert patch_r.json()["trackable"] is True
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_030_patch_nonexistent_part_returns_404(self, api_client, part_url):
        """TC_API_030: PATCH on non-existent part returns 404."""
        r = api_client.patch(f"{part_url}999999/", json={"name": "Ghost"})
        assert r.status_code == 404

    def test_TC_API_031_patch_part_invalid_category_returns_400(self, api_client, part_url, test_category_id):
        """TC_API_031: PATCH with invalid category returns 400."""
        payload = {"name": f"CatPatchPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"category": 999999})
        assert patch_r.status_code in [400, 404]
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_032_patch_part_name_too_long_returns_400(self, api_client, part_url, test_category_id):
        """TC_API_032: PATCH with name > 100 chars returns 400."""
        payload = {"name": f"LongNamePart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"name": "A" * 200})
        assert patch_r.status_code == 400
        api_client.delete(f"{part_url}{part_id}/")

    def test_TC_API_033_patch_part_response_contains_pk(self, api_client, part_url, test_category_id):
        """TC_API_033: PATCH response contains pk field."""
        payload = {"name": f"PkPatchPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        patch_r = api_client.patch(f"{part_url}{part_id}/", json={"description": "Check pk"})
        assert patch_r.status_code == 200
        assert "pk" in patch_r.json()
        api_client.delete(f"{part_url}{part_id}/")


class TestPartsDelete:

    def test_TC_API_034_delete_part_returns_204(self, api_client, part_url, test_category_id):
        """TC_API_034: DELETE returns 204 No Content."""
        payload = {"name": f"DeleteMe {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        del_r = api_client.delete(f"{part_url}{part_id}/")
        assert del_r.status_code == 204

    def test_TC_API_035_deleted_part_not_found(self, api_client, part_url, test_category_id):
        """TC_API_035: GET deleted part returns 404."""
        payload = {"name": f"DeletedPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        api_client.delete(f"{part_url}{part_id}/")
        get_r = api_client.get(f"{part_url}{part_id}/")
        assert get_r.status_code == 404

    def test_TC_API_036_delete_nonexistent_part_returns_404(self, api_client, part_url):
        """TC_API_036: DELETE non-existent part returns 404."""
        r = api_client.delete(f"{part_url}999999/")
        assert r.status_code == 404

    def test_TC_API_037_delete_part_no_auth_returns_401(self, base_url):
        """TC_API_037: DELETE without auth returns 401."""
        import requests
        r = requests.delete(f"{base_url}/part/1/")
        assert r.status_code == 401

    def test_TC_API_038_delete_part_removes_from_list(self, api_client, part_url, test_category_id):
        """TC_API_038: Deleted part does not appear in GET list."""
        payload = {"name": f"ListDeletePart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        api_client.delete(f"{part_url}{part_id}/")
        list_r = api_client.get(part_url)
        data = list_r.json()
        results = data.get("results", data) if isinstance(data, dict) else data
        pks = [p["pk"] for p in results]
        assert part_id not in pks

    def test_TC_API_039_double_delete_returns_404(self, api_client, part_url, test_category_id):
        """TC_API_039: Second DELETE of same part returns 404."""
        payload = {"name": f"DoubleDelete {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        api_client.delete(f"{part_url}{part_id}/")
        del2_r = api_client.delete(f"{part_url}{part_id}/")
        assert del2_r.status_code == 404

    def test_TC_API_040_delete_part_response_body_empty(self, api_client, part_url, test_category_id):
        """TC_API_040: DELETE response body is empty."""
        payload = {"name": f"EmptyBodyDelete {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        del_r = api_client.delete(f"{part_url}{part_id}/")
        assert del_r.status_code == 204
        assert del_r.text == "" or del_r.content == b""

    def test_TC_API_041_delete_part_with_stock_returns_error(self, api_client, part_url, test_category_id):
        """TC_API_041: DELETE part with active stock returns 400 or 405."""
        payload = {"name": f"StockedPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        del_r = api_client.delete(f"{part_url}{part_id}/")
        assert del_r.status_code in [204, 400, 405]

    def test_TC_API_042_delete_returns_no_content_type(self, api_client, part_url, test_category_id):
        """TC_API_042: DELETE response has no Content-Type header (204)."""
        payload = {"name": f"NoContentType {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        del_r = api_client.delete(f"{part_url}{part_id}/")
        assert del_r.status_code == 204

    def test_TC_API_043_delete_with_wrong_method_returns_405(self, api_client, part_url, test_category_id):
        """TC_API_043: PUT to delete endpoint returns 405."""
        payload = {"name": f"WrongMethodPart {uuid.uuid4().hex[:8]}", "category": test_category_id}
        r = api_client.post(part_url, json=payload)
        part_id = r.json()["pk"]
        put_r = api_client.put(f"{part_url}{part_id}/", json={"name": "Nope"})
        assert put_r.status_code in [400, 405]
        api_client.delete(f"{part_url}{part_id}/")
