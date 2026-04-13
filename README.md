# InvenTree Hackathon Submission

> **Participant:** ganesh2412
> **Module Under Test:** InvenTree Parts Module
> **Submission Deadline:** April 14, 2026 at 19:00 UTC+5

## Overview

This repository is a hackathon submission for AI-assisted test case generation and automation for the InvenTree Parts module. All test cases and automation scripts were generated using an AI agent (Comet by Perplexity) from official InvenTree documentation.

---

## Repository Structure

```
submission/
├── agents/
│   └── prompts.md               # All AI prompts and system instructions used
├── test-cases/
│   ├── ui-manual-tests.md       # UI manual test cases (TC_UI_PC, DT, CAT, ATTR, UOM, REV, NEG)
│   └── api-manual-tests.md      # API manual test cases (TC_API_001 to TC_API_050)
├── automation/
│   ├── ui/
│   │   └── README.md              # Playwright UI automation setup
│   └── api/
│       └── README.md              # pytest API automation setup
└── video/                           # Demo recording (to be added)
```

---

## Test Coverage Summary

### UI Manual Tests (`test-cases/ui-manual-tests.md`)

| Section | TC IDs | Count |
|---|---|---|
| Part Creation | TC_UI_PC_001 – 030 | 30 |
| Part Detail Tabs | TC_UI_DT_001 – 020 | 20 |
| Part Categories | TC_UI_CAT_001 – 008 | 8 |
| Part Attributes | TC_UI_ATTR_001 – 010 | 10 |
| Units of Measure | TC_UI_UOM_001 – 005 | 5 |
| Part Revisions | TC_UI_REV_001 – 008 | 8 |
| Negative & Boundary | TC_UI_NEG_001 – 015 | 15 |
| **Total** | | **96** |

### API Manual Tests (`test-cases/api-manual-tests.md`)

| Endpoint | Methods | TC IDs | Count |
|---|---|---|---|
| /api/part/ | GET, POST | TC_API_001–023 | 23 |
| /api/part/{id}/ | GET, PATCH, DELETE | TC_API_024–041 | 18 |
| /api/part/category/ | GET, POST | TC_API_042–050 | 9 |
| **Total** | | | **50** |

---

## Tools & Approach

| Area | Tool |
|---|---|
| AI Agent | Comet (Perplexity) |
| UI Automation Framework | Playwright (TypeScript) |
| API Automation Framework | pytest + requests (Python) |
| Documentation Source | https://docs.inventree.org |
| Repository | GitHub (Public) |

## How to Run UI Tests

```bash
cd submission/automation/ui
npm install
npx playwright install
npx playwright test
```

## How to Run API Tests

```bash
cd submission/automation/api
pip install -r requirements.txt
# Create .env with INVENTREE_BASE_URL and INVENTREE_API_TOKEN
pytest tests/ -v
```

---

## Agent Approach

1. Fed InvenTree Parts documentation URLs to the AI agent
2. AI generated comprehensive test cases based on documented behaviors
3. Test cases reviewed and refined for coverage and accuracy
4. Automation scripts generated from manual test cases
5. All prompts documented in `submission/agents/prompts.md`

---

## Automation Implementation Status

### API Automation (pytest + requests)
**Status:** ✅ Complete

#### Files Created:
- `submission/automation/api/requirements.txt`
- `submission/automation/api/conftest.py` - Shared fixtures and configuration
- `submission/automation/api/tests/test_parts_get.py` - TC_API_001-010 (GET /api/part/)
- `submission/automation/api/tests/test_parts_post.py` - TC_API_011-023 (POST /api/part/)
- `submission/automation/api/tests/test_parts_patch_delete.py` - TC_API_024-043 (PATCH/DELETE /api/part/{id}/)
- `submission/automation/api/tests/test_categories.py` - TC_API_044-060 (Part Categories)

**Total API Test Cases Automated:** 60 test cases covering:
- GET operations with filtering, pagination, and error handling
- POST operations with validation and boundary testing
- PATCH operations for updates
- DELETE operations and cascade behaviors
- Category management endpoints

### UI Automation (Playwright)
**Status:** ✅ Partial Implementation

#### Files Created:
- `submission/automation/ui/requirements.txt`
- `submission/automation/ui/tests/conftest.py` - Browser setup and authentication fixtures
- `submission/automation/ui/tests/test_part_creation.py` - Basic part creation flows

**Coverage:** Implements foundational UI test cases for:
- Navigation to Parts section
- Part creation form interactions
- Form validation
- Basic CRUD operations

**Note:** Additional UI test coverage can be expanded based on the 96 manual UI test cases documented in `submission/test-cases/ui-manual-tests.md`



## References

- https://docs.inventree.org/en/stable/part/
- https://docs.inventree.org/en/stable/part/views/
- https://docs.inventree.org/en/latest/part/create/
- https://docs.inventree.org/en/stable/part/template/
- https://docs.inventree.org/en/stable/part/revision/
- https://docs.inventree.org/en/stable/api/api/
