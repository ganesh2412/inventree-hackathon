# API Automation

This folder contains API automation test scripts for the InvenTree Parts module.

## Framework
- Tool: pytest + requests (Python)
- Coverage: Parts CRUD, Category CRUD, filtering, pagination, auth validation
- Test IDs: TC_API_001 to TC_API_060

## Prerequisites
- Python 3.8+
- InvenTree running at `http://localhost` (Docker Compose setup)
- Valid API token

## Setup
```bash
cd submission/automation/api
pip install -r requirements.txt
```

## Environment Setup
Copy `.env.example` to `.env` and fill in your values:
```bash
cp .env.example .env
```

Or set environment variables:
```
INVENTREE_BASE_URL=http://localhost
INVENTREE_API_TOKEN=your-token-here
```

Get your API token from: `http://localhost/api/user/token/` (when logged in as admin)

## Run Tests
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_parts_get.py -v
pytest tests/test_parts_post.py -v
pytest tests/test_parts_patch_delete.py -v
pytest tests/test_categories.py -v

# Run with output on failure
pytest tests/ -v --tb=short
```

## Test Files
- `tests/test_parts_get.py` - GET /api/part/ tests (TC_API_001 to TC_API_010)
- `tests/test_parts_post.py` - POST /api/part/ tests (TC_API_011 to TC_API_023)
- `tests/test_parts_patch_delete.py` - PATCH and DELETE tests (TC_API_024 to TC_API_043)
- `tests/test_categories.py` - Category endpoint tests (TC_API_044 to TC_API_060)
- `tests/conftest.py` - Shared fixtures (api_client, base_url, part_url, test_category_id)
