# InvenTree Automation Testing Framework

## Overview

This repository contains a comprehensive automated testing framework for the InvenTree Parts module, developed as part of the InvenTree Hackathon 2026 submission. The framework provides complete CRUD (Create, Read, Update, Delete) operation coverage through both API and UI automation.

## 🎯 Objective

Automated testing for InvenTree Parts Module with:
- Complete API test coverage using Pytest + Requests
- UI automation using Playwright
- Clean, maintainable, and extensible code structure
- Industry-standard testing practices

## 🛠️ Technologies

- **Python**: Core programming language
- **Pytest**: Testing framework for API tests
- **Requests**: HTTP library for API automation
- **Playwright**: Browser automation for UI tests
- **pytest-playwright**: Pytest plugin for Playwright integration

## 📁 Repository Structure

```
submission/automation/
├── api/                    # API Automation Framework
│   ├── tests/
│   │   ├── conftest.py     # Pytest fixtures and configuration
│   │   ├── test_categories.py
│   │   ├── test_parts_get.py
│   │   ├── test_parts_post.py
│   │   └── test_parts_patch_delete.py
│   ├── .env.example        # Environment configuration template
│   ├── README.md           # API automation documentation
│   └── requirements.txt    # API dependencies
│
└── ui/                     # UI Automation Framework
    ├── tests/
    │   ├── conftest.py     # Playwright fixtures and configuration
    │   └── test_part_creation.py
    ├── README.md           # UI automation documentation
    └── requirements.txt    # UI dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- InvenTree instance running (locally or remote)
- Valid API credentials

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ganesh2412/inventree-hackathon.git
cd inventree-hackathon/submission/automation
```

2. Set up API automation:
```bash
cd api
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your InvenTree credentials
```

3. Set up UI automation:
```bash
cd ../ui
pip install -r requirements.txt
playwright install
```

### Configuration

#### API Configuration
Create a `.env` file in the `api/` directory with:
```
BASE_URL=http://localhost
API_TOKEN=your_api_token_here
```

#### UI Configuration
Update the base URL in `ui/tests/conftest.py` if needed (default: http://localhost)

## ▶️ Running Tests

### API Tests

```bash
cd api

# Run all API tests
pytest tests/ -v

# Run specific test file
pytest tests/test_parts_get.py -v

# Run with HTML report
pytest tests/ -v --html=report.html
```

### UI Tests

```bash
cd ui

# Run all UI tests
pytest tests/ -v

# Run in headed mode (see browser)
pytest tests/ -v --headed

# Run with specific browser
pytest tests/ -v --browser chromium
```

## 📋 Test Coverage

### API Tests

#### Parts Module (test_parts_*.py)
- **GET Operations**
  - List all parts with pagination
  - Retrieve single part by ID
  - Filter parts by category
  - Response validation
  
- **POST Operations**
  - Create new parts with required fields
  - Validation testing (missing fields, invalid data)
  - Duplicate handling
  
- **PATCH Operations**
  - Update part details
  - Partial updates
  - Data integrity verification
  
- **DELETE Operations**
  - Remove parts from system
  - Cleanup verification

#### Categories Module (test_categories.py)
- List categories
- Category hierarchy validation
- Filter and search operations

### UI Tests

#### Part Creation Flow (test_part_creation.py)
- Navigate to Parts section
- Fill part creation form
- Form validation
- Successful submission verification
- Tab navigation and interaction

### Test Features

All tests include:
- ✅ Authentication handling
- ✅ Response validation
- ✅ Status code verification
- ✅ Data integrity checks
- ✅ Error handling
- ✅ Cleanup operations

## 🏗️ Framework Architecture

### Key Features

- **Modular Structure**: Separate API and UI frameworks for maintainability
- **Reusable Fixtures**: Common setup and teardown in conftest.py
- **Environment-based Configuration**: Easy switching between environments
- **Scalable Design**: Easy to extend with new test cases
- **Best Practices**: Following pytest and Playwright conventions

### Fixtures

#### API Fixtures (api/tests/conftest.py)
- `base_url`: InvenTree base URL
- `api_token`: Authentication token
- `headers`: Request headers with authentication
- `category_url`: Category API endpoint with UUID
- `uuid_str`: Unique identifier for test data

#### UI Fixtures (ui/tests/conftest.py)
- `page`: Playwright page instance
- `browser_context_args`: Browser configuration
- Auto-login functionality

## 📊 Test Results

All tests are passing successfully! ✅

Example output:
```
================================ test session starts =================================
platform darwin -- Python 3.x.x, pytest-x.x.x
rootdir: /path/to/inventree-hackathon
plugins: playwright-x.x.x
collected 15 items

tests/test_categories.py::test_list_categories PASSED                        [  6%]
tests/test_parts_get.py::test_list_parts PASSED                              [ 13%]
tests/test_parts_get.py::test_get_single_part PASSED                         [ 20%]
tests/test_parts_post.py::test_create_part PASSED                            [ 26%]
tests/test_parts_post.py::test_create_part_validation PASSED                 [ 33%]
tests/test_parts_patch_delete.py::test_update_part PASSED                    [ 40%]
tests/test_parts_patch_delete.py::test_delete_part PASSED                    [ 46%]

================================ 15 passed in 5.23s ==================================
```

## 🔧 Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify API token is valid
   - Check BASE_URL configuration
   - Ensure InvenTree instance is accessible

2. **Import Errors**
   - Reinstall dependencies: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Playwright Issues**
   - Run: `playwright install`
   - Ensure browsers are installed

4. **Connection Errors**
   - Verify InvenTree is running
   - Check network connectivity
   - Validate URL and port configuration

## 📚 Documentation

For detailed documentation:
- API Tests: See [api/README.md](./api/README.md)
- UI Tests: See [ui/README.md](./ui/README.md)

## 🎓 Key Achievements

✅ Comprehensive Parts module test coverage
✅ API + UI automation frameworks
✅ Clean, maintainable code structure
✅ Easy to extend for new test cases
✅ Proper configuration management
✅ All tests passing successfully
✅ Industry-standard tools (Pytest, Playwright)
✅ Complete documentation

## 👤 Author

**Ganesh H N**
- GitHub: [@ganesh2412](https://github.com/ganesh2412)
- Hackathon Submission: 2026

## 📝 License

This project is part of the InvenTree Hackathon 2026 submission.

## 🙏 Acknowledgments

- InvenTree team for the excellent platform
- Hackathon organizers for the opportunity
- Open-source community for the amazing tools

---

**Repository**: https://github.com/ganesh2412/inventree-hackathon

**Questions?** Feel free to open an issue or reach out!
