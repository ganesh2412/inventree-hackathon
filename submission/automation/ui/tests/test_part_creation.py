import pytest
from playwright.sync_api import Page, expect


def test_navigate_to_parts(authenticated_page: Page):
  """Test navigating to Parts section."""
  authenticated_page.click("text=Parts")
    expect(authenticated_page).to_have_url("**/web/part/**")

def test_create_part_button_visible(authenticated_page: Page):
  """Test Create Part button is visible."""
  authenticated_page.goto("http://localhost/web/part")
  expect(authenticated_page.locator("text=Create Part").or_(authenticated_page.locator("button:has-text('New')"))).to_be_visible()


def test_create_part_form_opens(authenticated_page: Page):
  """Test Create Part form opens."""
  authenticated_page.goto("http://localhost/web/part")
  authenticated_page.click("button:has-text('Create')")
  expect(authenticated_page.locator("input[name='name']")).to_be_visible(timeout=3000)


def test_part_name_field_required(authenticated_page: Page):
  """Test Part name field is required."""
  authenticated_page.goto("http://localhost/web/part")
  authenticated_page.click("button:has-text('Create')")
  authenticated_page.click("button[type='submit']")
  # Check for validation message or form still open
  expect(authenticated_page.locator("input[name='name']")).to_be_visible()


def test_create_part_with_name(authenticated_page: Page):
  """Test creating a part with only name."""
  authenticated_page.goto("http://localhost/web/part")
  authenticated_page.click("button:has-text('Create')")
  authenticated_page.fill("input[name='name']", "UI Test Part")
  authenticated_page.click("button[type='submit']")
  expect(authenticated_page.locator("text=UI Test Part")).to_be_visible(timeout=5000)


def test_create_part_with_description(authenticated_page: Page):
  """Test creating a part with name and description."""
  authenticated_page.goto("http://localhost/web/part")
  authenticated_page.click("button:has-text('Create')")
  authenticated_page.fill("input[name='name']", "Part with Description")
  authenticated_page.fill("textarea[name='description']", "This is a test description")
  authenticated_page.click("button[type='submit']")
  expect(authenticated_page.locator("text=Part with Description")).to_be_visible(timeout=5000)


def test_part_appears_in_list(authenticated_page: Page):
  """Test created part appears in parts list."""
  authenticated_page.goto("http://localhost/web/part")
  expect(authenticated_page.locator("text=UI Test Part")).to_be_visible()
