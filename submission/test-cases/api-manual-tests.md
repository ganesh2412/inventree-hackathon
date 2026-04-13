# API Manual Test Cases – InvenTree Parts Module

## Scope
REST API endpoints for the InvenTree Parts module.

## References
- https://docs.inventree.org/en/stable/api/api/
- https://docs.inventree.org/en/stable/part/

## Base URL
`http://<your-inventree-host>/api/`

## Authentication
All requests require a valid API token in the header:
`Authorization: Token <your-api-token>`

## Preconditions
- InvenTree instance is running and accessible
- Valid API token available
- At least one Part Category exists
- Test data parts available for GET/PATCH/DELETE tests

---

## Parts Endpoint – GET /api/part/

| TC ID | Endpoint | Method | Description | Request | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| TC_API_001 | /api/part/ | GET | List all parts | No body | 200 | JSON array of part objects |
| TC_API_002 | /api/part/ | GET | List parts with search query | ?search=resistor | 200 | Filtered parts matching search term |
| TC_API_003 | /api/part/ | GET | List parts filtered by category | ?category=1 | 200 | Parts belonging to specified category |
| TC_API_004 | /api/part/ | GET | List active parts only | ?active=true | 200 | Only active parts returned |
| TC_API_005 | /api/part/ | GET | List inactive parts only | ?active=false | 200 | Only inactive parts returned |
| TC_API_006 | /api/part/ | GET | Paginate results | ?limit=10&offset=0 | 200 | 10 results returned with count and next/previous links |
| TC_API_007 | /api/part/ | GET | List assembly parts only | ?assembly=true | 200 | Only assembly parts returned |
| TC_API_008 | /api/part/ | GET | List purchaseable parts | ?purchaseable=true | 200 | Only purchaseable parts returned |
| TC_API_009 | /api/part/ | GET | Request without authentication | No token | 401 | Unauthorized error response |
| TC_API_010 | /api/part/ | GET | List with invalid filter value | ?active=notabool | 200 or 400 | Appropriate response; no server crash |

---

## Parts Endpoint – POST /api/part/

| TC ID | Endpoint | Method | Description | Request | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| TC_API_011 | /api/part/ | POST | Create part with all required fields | {name, category} | 201 | Created part object with assigned ID |
| TC_API_012 | /api/part/ | POST | Create part with all optional fields | Full part payload | 201 | Part created with all fields saved |
| TC_API_013 | /api/part/ | POST | Create part with missing name | {category: 1} | 400 | Validation error for missing name |
| TC_API_014 | /api/part/ | POST | Create part with missing category | {name: "Test"} | 400 | Validation error for missing category |
| TC_API_015 | /api/part/ | POST | Create part with invalid category ID | {name: "Test", category: 99999} | 400 | Error: category does not exist |
| TC_API_016 | /api/part/ | POST | Create part with duplicate IPN (when unique enforced) | Existing IPN value | 400 | Error: duplicate IPN |
| TC_API_017 | /api/part/ | POST | Create part with empty string name | {name: "", category: 1} | 400 | Validation error for blank name |
| TC_API_018 | /api/part/ | POST | Create part without authentication | Valid body, no token | 401 | Unauthorized error |
| TC_API_019 | /api/part/ | POST | Create virtual part | {name, category, virtual: true} | 201 | Part created with virtual=true |
| TC_API_020 | /api/part/ | POST | Create assembly part | {name, category, assembly: true} | 201 | Part created with assembly=true |
| TC_API_021 | /api/part/ | POST | Create trackable part | {name, category, trackable: true} | 201 | Part created with trackable=true |
| TC_API_022 | /api/part/ | POST | Create part with very long name at boundary | Max length name string | 201 | Part created successfully |
| TC_API_023 | /api/part/ | POST | Create part with name exceeding max length | Name > max length | 400 | Validation error for field too long |

---

## Parts Endpoint – GET /api/part/{id}/

| TC ID | Endpoint | Method | Description | Request | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| TC_API_024 | /api/part/{id}/ | GET | Retrieve existing part by ID | Valid part ID | 200 | Full part object |
| TC_API_025 | /api/part/{id}/ | GET | Retrieve non-existent part | ID: 999999 | 404 | Not found error |
| TC_API_026 | /api/part/{id}/ | GET | Retrieve part without authentication | Valid ID, no token | 401 | Unauthorized error |
| TC_API_027 | /api/part/{id}/ | GET | Retrieve part with string ID | ID: "abc" | 404 or 400 | Error response |
| TC_API_028 | /api/part/{id}/ | GET | Verify response contains all expected fields | Valid part ID | 200 | Response includes: id, name, description, category, active, assembly, virtual, trackable, purchaseable, salable, IPN, revision |

---

## Parts Endpoint – PATCH /api/part/{id}/

| TC ID | Endpoint | Method | Description | Request | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| TC_API_029 | /api/part/{id}/ | PATCH | Update part name | {name: "Updated Name"} | 200 | Updated part object |
| TC_API_030 | /api/part/{id}/ | PATCH | Update part description | {description: "New desc"} | 200 | Updated description in response |
| TC_API_031 | /api/part/{id}/ | PATCH | Set part as inactive | {active: false} | 200 | Part active=false in response |
| TC_API_032 | /api/part/{id}/ | PATCH | Set part as active | {active: true} | 200 | Part active=true in response |
| TC_API_033 | /api/part/{id}/ | PATCH | Update with empty name | {name: ""} | 400 | Validation error |
| TC_API_034 | /api/part/{id}/ | PATCH | Update non-existent part | ID: 999999 | 404 | Not found error |
| TC_API_035 | /api/part/{id}/ | PATCH | Update without authentication | Valid body, no token | 401 | Unauthorized error |
| TC_API_036 | /api/part/{id}/ | PATCH | Update read-only field (id) | {id: 999} | 200 | Read-only field ignored; ID unchanged |

---

## Parts Endpoint – DELETE /api/part/{id}/

| TC ID | Endpoint | Method | Description | Request | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| TC_API_037 | /api/part/{id}/ | DELETE | Delete part with no dependencies | Valid part ID, no stock | 204 | No content; part removed |
| TC_API_038 | /api/part/{id}/ | DELETE | Delete part with active stock | Part with stock items | 400 | Error: cannot delete part with stock |
| TC_API_039 | /api/part/{id}/ | DELETE | Delete part used in BOM | Part used in BOM | 400 | Error: cannot delete part in use |
| TC_API_040 | /api/part/{id}/ | DELETE | Delete non-existent part | ID: 999999 | 404 | Not found error |
| TC_API_041 | /api/part/{id}/ | DELETE | Delete without authentication | Valid ID, no token | 401 | Unauthorized error |

---

## Part Category Endpoint – GET /api/part/category/

| TC ID | Endpoint | Method | Description | Request | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| TC_API_042 | /api/part/category/ | GET | List all categories | No body | 200 | JSON array of category objects |
| TC_API_043 | /api/part/category/ | GET | Filter categories by parent | ?parent=1 | 200 | Only subcategories of parent returned |
| TC_API_044 | /api/part/category/ | GET | Search categories by name | ?search=electronics | 200 | Matching categories returned |
| TC_API_045 | /api/part/category/ | GET | Request without authentication | No token | 401 | Unauthorized error |

---

## Part Category Endpoint – POST /api/part/category/

| TC ID | Endpoint | Method | Description | Request | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| TC_API_046 | /api/part/category/ | POST | Create category with valid name | {name: "New Category"} | 201 | Created category object |
| TC_API_047 | /api/part/category/ | POST | Create subcategory with valid parent | {name: "Sub", parent: 1} | 201 | Subcategory created under parent |
| TC_API_048 | /api/part/category/ | POST | Create category with missing name | {description: "test"} | 400 | Validation error for missing name |
| TC_API_049 | /api/part/category/ | POST | Create category with invalid parent | {name: "X", parent: 99999} | 400 | Error: parent does not exist |
| TC_API_050 | /api/part/category/ | POST | Create category without authentication | Valid body, no token | 401 | Unauthorized error |
