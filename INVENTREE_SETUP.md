# InvenTree Setup Guide for Testing

## 

## Step 0: Clone Repository (First Time Only)

**IMPORTANT:** Before running tests, you need to clone the repository to your local machine!

```bash
# Navigate to your preferred directory
cd ~/Desktop  # or ~/Documents or wherever you want

# Clone the repository
git clone https://github.com/ganesh2412/inventree-hackathon.git

# Navigate into the repository
cd inventree-hackathon

# Verify files exist
ls -la submission/automation/
```

You should see:
```
submission/automation/
├── api/
│   ├── requirements.txt
│   ├── conftest.py
│   └── tests/
└── ui/
    ├── requirements.txt
    └── tests/
```

Quick Setup Commands

Based on your Docker setup, here are the exact commands to get InvenTree ready for testing:

### Step 1: Create Superuser

```bash
# Enter the InvenTree container
docker compose exec inventree-server bash

# Navigate to InvenTree manage.py location
cd /home/inventree/src/backend/InvenTree

# Create superuser
python3 manage.py createsuperuser

# Enter details when prompted:
# Username: admin
# Email: admin@example.com
# Password: admin123 (or your choice)
# Password (again): admin123
```

### Step 2: Verify InvenTree is Running

```bash
# Exit container
exit

# Check InvenTree is accessible
curl http://localhost:8000

# Or open in browser:
# http://localhost:8000
```

### Step 3: Get API Token

1. **Open Browser:** http://localhost:8000
2. **Login:** 
   - Username: admin
   - Password: admin123 (or what you set)
3. **Navigate to:** User Icon (top right) → Settings → API Tokens
4. **Click:** "Generate New Token"
5. **Copy Token:** Save it for testing

### Step 4: Create Test Category

```bash
# In container
docker compose exec inventree-server bash
cd /home/inventree/src/backend/InvenTree

# Create test category via Django shell
python3 manage.py shell
```

```python
# In Python shell:
from part.models import PartCategory

cat = PartCategory.objects.create(
    name="Test Category",
    description="Category for automated testing"
)
print(f"Created category with ID: {cat.id}")
exit()
```

---

## Running Automation Tests

### API Tests Setup

```bash
# On your local machine (not in container)
cd ~/inventree-hackathon/submission/automation/api

# Install dependencies
pip3 install -r requirements.txt

# Create .env file with your token
cat > .env << EOF
INVENTREE_BASE_URL=http://localhost:8000
INVENTREE_API_TOKEN=YOUR_TOKEN_HERE
EOF

# Replace YOUR_TOKEN_HERE with actual token from Step 3
```

### Run API Tests

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

### UI Tests Setup

```bash
cd ~/inventree-hackathon/submission/automation/ui

# Install dependencies
pip3 install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Run UI Tests

```bash
# Update conftest.py with correct URL and credentials
# Edit: submission/automation/ui/tests/conftest.py
# Update login credentials to match your superuser

# Run UI tests (visible browser)
pytest tests/ -v --headed

# Run UI tests (headless)
pytest tests/ -v
```

---

## Troubleshooting

### Issue: manage.py not found

**Solution:** Use the full path:
```bash
python3 /home/inventree/src/backend/InvenTree/manage.py createsuperuser
```

### Issue: Permission denied

**Solution:** Check you're in container as root:
```bash
docker compose exec -u root inventree-server bash
```

### Issue: API returns 401 Unauthorized

**Solution:** 
1. Verify token is correct
2. Check token hasn't expired
3. Regenerate token if needed

### Issue: Tests fail with "Category not found"

**Solution:** Create test category first (see Step 4)

### Issue: Port 8000 not accessible

**Solution:**
```bash
# Check Docker containers
docker compose ps

# Check port mapping
docker compose port inventree-server 8000

# Restart if needed
docker compose restart
```

---

## Useful Commands

### InvenTree Management

```bash
# View logs
docker compose logs -f inventree-server

# Restart InvenTree
docker compose restart inventree-server

# Stop InvenTree
docker compose stop

# Start InvenTree
docker compose up -d
```

### Database Operations

```bash
# Run migrations
docker compose exec inventree-server python3 /home/inventree/src/backend/InvenTree/manage.py migrate

# Create demo data
docker compose exec inventree-server python3 /home/inventree/src/backend/InvenTree/manage.py populate
```

### Django Shell Access

```bash
docker compose exec inventree-server python3 /home/inventree/src/backend/InvenTree/manage.py shell
```

---

## Test Data Setup

For comprehensive testing, create sample data:

```python
# In Django shell
from part.models import Part, PartCategory

# Create category
cat = PartCategory.objects.create(name="Electronics", description="Electronic parts")

# Create sample parts
Part.objects.create(
    name="Resistor 100 Ohm",
    description="Standard resistor",
    category=cat,
    active=True,
    purchaseable=True
)

Part.objects.create(
    name="Capacitor 10uF",
    description="Electrolytic capacitor",
    category=cat,
    active=True,
    salable=True
)

print(f"Created {Part.objects.count()} parts")
```

---

## Demo Recording Tips

### What to Show:

1. **Terminal:** 
   - Show docker ps output
   - Show InvenTree running

2. **Browser:**
   - Login to InvenTree UI
   - Navigate Parts section
   - Show test data

3. **VS Code/Terminal:**
   - Show test files
   - Run pytest commands
   - Show test results

4. **Results:**
   - Show HTML report
   - Show pass/fail counts

### Screen Recording:

```bash
# Linux - Using SimpleScreenRecorder
sudo apt install simplescreenrecorder

# Or use OBS Studio
sudo apt install obs-studio
```

---

## Quick Verification Checklist

- [ ] InvenTree container running (`docker compose ps`)
- [ ] Superuser created (admin/admin123)
- [ ] Can login to http://localhost:8000
- [ ] API token generated and copied
- [ ] Test category created
- [ ] .env file created with correct token
- [ ] API tests run successfully
- [ ] UI tests setup complete
- [ ] At least one test passes

---

## Next Steps

1. ✅ Complete setup (Steps 1-4)
2. 🧪 Run API tests
3. 🎭 Run UI tests
4. 📹 Record demo (optional)
5. 📊 Generate test reports
6. 🚀 Submit to hackathon!

**Good luck with your testing!** 🍀
