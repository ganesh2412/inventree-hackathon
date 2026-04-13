import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
  """Configure browser context."""
  return {
    **browser_context_args,
    "viewport": {"width": 1920, "height": 1080},
  }


@pytest.fixture
def inventree_page(page: Page):
  """Navigate to InvenTree login page."""
  page.goto("http://localhost")
  return page


@pytest.fixture
def authenticated_page(inventree_page: Page):
  """Log in to InvenTree and return authenticated page."""
  # Update credentials based on your test environment
  inventree_page.fill("input[placeholder='Your username']", "admin")
  inventree_page.fill("input[placeholder='Your password']", "admin")
  inventree_page.click("button[type='submit']")
  inventree_page.wait_for_url("**/web**", timeout=5000)
  return inventree_page
