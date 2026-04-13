# Demo Preparation Guide

## Quick Start: Running the Tests

### Prerequisites

1. **InvenTree Instance Running**
   - You need a running InvenTree server (local or remote)
   - Default: `http://localhost:8000`
   - Must have API access enabled

2. **API Token**
   - Log into InvenTree web interface
   - Go to User Settings → API Tokens
   - Create a new token and copy it

---

## Part 1: Running API Tests

### Setup (One-time)

```bash
# Navigate to API automation folder
cd ~/inventree-hackathon/submission/automation/api

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
INVENTREE_BASE_URL=http://localhost:8000
INVENTREE_API_TOKEN=your_token_here
EOF
```

### Run Tests

```bash
# Run all API tests
pytest tests/ -v

# Run specific test file
pytest tests/test_parts_get.py -v

# Run with detailed output
pytest tests/ -v -s

# Generate HTML report
pytest tests/ --html=report.html --self-contained-html
```

**Expected Output:**
- ✅ 60+ test cases should execute
- Some may fail if InvenTree instance doesn't have test data
- Look for overall pass rate

---

## Part 2: Running UI Tests

### Setup (One-time)

```bash
# Navigate to UI automation folder
cd ~/inventree-hackathon/submission/automation/ui

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Run Tests

```bash
# Run all UI tests (headless)
pytest tests/ -v

# Run with browser visible (headed mode)
pytest tests/ -v --headed

# Run specific test
pytest tests/test_part_creation.py -v --headed

# Generate HTML report
pytest tests/ --html=ui_report.html --self-contained-html
```

**Expected Output:**
- Browser will open and navigate InvenTree UI
- Tests will create parts, navigate menus
- Check for authentication success

---

## Demo Script for Presentation

### Introduction (2 minutes)

**Say:**
> "This is my InvenTree Parts Module testing submission. I used AI agent Comet by Perplexity to generate comprehensive test cases and automation scripts from InvenTree documentation."

**Show:**
- GitHub repository: https://github.com/ganesh2412/inventree-hackathon
- README with test coverage summary

### Part 1: Test Cases (3 minutes)

**Say:**
> "I created 146 total test cases: 96 UI manual tests and 50 API manual tests."

**Show:**
1. Navigate to `submission/test-cases/ui-manual-tests.md`
   - Show Part Creation section (30 cases)
   - Show Part Detail Tabs section (20 cases)
   - Highlight structured format with TC IDs

2. Navigate to `submission/test-cases/api-manual-tests.md`
   - Show GET /api/part/ section
   - Show POST /api/part/ section
   - Point out response validation, error handling

### Part 2: Automation - API Tests (4 minutes)

**Say:**
> "I automated all 60 API test cases using pytest and requests library."

**Show:**
1. Navigate to `submission/automation/api/tests/`
   - Show test_parts_get.py file structure
   - Highlight: conftest.py with fixtures

2. **Run live demo:**
   ```bash
   cd submission/automation/api
   pytest tests/test_parts_get.py -v
   ```

3. **Show results:**
   - Executed test count
   - Pass/fail status
   - Execution time

### Part 3: Automation - UI Tests (3 minutes)

**Say:**
> "I created UI automation framework using Playwright for browser testing."

**Show:**
1. Navigate to `submission/automation/ui/tests/`
   - Show test_part_creation.py
   - Explain authentication fixture

2. **Run live demo (if time permits):**
   ```bash
   cd submission/automation/ui
   pytest tests/test_part_creation.py -v --headed
   ```

3. **Show:**
   - Browser opening
   - Login automation
   - Part creation flow

### Part 4: AI Agent Approach (2 minutes)

**Say:**
> "All test cases were AI-generated. Let me show the prompts I used."

**Show:**
1. Navigate to `submission/agents/prompts.md`
2. Show Prompt 1: Documentation analysis
3. Show Prompt 2: Test case generation
4. Explain systematic approach

### Conclusion (1 minute)

**Say:**
> "This submission demonstrates:
> - Comprehensive test coverage (146 manual + 60+ automated)
> - Working automation frameworks for both API and UI
> - Systematic AI-driven approach
> - Production-ready test structure"

**Show:**
- Scroll through README showing automation status
- Final repository structure view

---

## Troubleshooting

### Tests Fail Due to Missing Data

**Solution:** Create test category first
```python
# Run this in Python console
import requests
headers = {"Authorization": "Token YOUR_TOKEN"}
data = {"name": "Test Category", "description": "For automated testing"}
response = requests.post(
    "http://localhost:8000/api/part/category/",
    json=data,
    headers=headers
)
print(f"Category ID: {response.json()['pk']}")
```

### InvenTree Not Running

**Quick Start:**
```bash
# If using Docker
docker run -d -p 8000:8000 inventree/inventree:latest

# Wait for startup, then access: http://localhost:8000
```

### Authentication Issues

- Verify API token is correct
- Check token has proper permissions
- Ensure InvenTree API is enabled in settings

---

## Pre-Demo Checklist

- [ ] InvenTree instance is running
- [ ] API token is generated and added to .env
- [ ] Dependencies installed (pip install -r requirements.txt)
- [ ] Playwright browsers installed (playwright install)
- [ ] Run tests once to verify they work
- [ ] Prepare HTML reports if needed
- [ ] GitHub repository is public and accessible
- [ ] README is up to date
- [ ] Practice demo flow (15 minutes total)

---

## Quick Demo Command Reference

```bash
# API Tests
cd ~/inventree-hackathon/submission/automation/api
pytest tests/ -v

# UI Tests (visible browser)
cd ~/inventree-hackathon/submission/automation/ui  
pytest tests/ -v --headed

# Generate HTML reports
pytest tests/ --html=report.html --self-contained-html
```

---

## Recording Demo Video

If you need to record:

1. **Screen Recording Tools:**
   - macOS: QuickTime Player (Cmd+Shift+5)
   - Linux: OBS Studio, SimpleScreenRecorder
   - Windows: Xbox Game Bar (Win+G)

2. **What to Record:**
   - GitHub repository overview (30 sec)
   - Test case files (1 min)
   - Running API tests (1 min)
   - Running UI tests with browser (1 min)
   - Results and reports (30 sec)

3. **Upload to:**
   - YouTube (unlisted)
   - Google Drive
   - Add link to README

---

## Support Commands

```bash
# Check Python version (need 3.8+)
python --version

# Check if pytest installed
pytest --version

# Check if playwright installed
playwright --version

# List all test cases
pytest --collect-only

# Run tests with coverage
pytest tests/ --cov=. --cov-report=html
```
