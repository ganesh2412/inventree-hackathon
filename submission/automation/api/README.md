# API Automation

This folder contains API automation test scripts for the InvenTree Parts module.

## Framework
- Tool: pytest + requests (Python)
- Coverage: Parts CRUD, Category CRUD, filtering, pagination, auth validation

## Setup
```bash
pip install -r requirements.txt
```

## Run Tests
```bash
pytest tests/ -v
```

## Environment Setup
Create a `.env` file with:
```
INVENTREE_BASE_URL=http://localhost:8000
INVENTREE_API_TOKEN=your-token-here
```

## Test Files
- `tests/test_parts_get.py` - GET /api/part/ tests
- `tests/test_parts_post.py` - POST /api/part/ tests
- `tests/test_parts_patch_delete.py` - PATCH and DELETE tests
- `tests/test_categories.py` - Category endpoint tests

> Automation scripts will be added in the next phase of the hackathon.
