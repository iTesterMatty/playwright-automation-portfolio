from playwright.sync_api import Page, expect
import pytest

# Runs automatically once before any tests start
# Configures the global test ID strategy for the whole file
@pytest.fixture(scope="module", autouse=True)
def configure_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

def login_to_sauce_demo(page: Page, username: str="standard_user", password: str="secret_sauce"):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


def test_login_and_shop(page: Page):
    
    # Login with correct credentials
    login_to_sauce_demo(page)

    # Buy a backpack item
    item = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    item.get_by_role("button", name="Add to cart").click()

    # Go to shopping cart
    page.locator(".shopping_cart_link").click()

    # --- ASSERT ---
    # Check if we are on the Shopping cart page, and if the backpack is in our cart
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

def test_sort_product_by_price(page: Page):

    # Login with correct credentials
    login_to_sauce_demo(page)

    # Choose a Price (low to high) option from a dropdown
    page.get_by_role("combobox").select_option(label="Price (low to high)")

    # --- ASSERT ---
    # Check if the first item is with the lowest price $7.99
    expect(page.locator(".inventory_item_name").first).to_have_text("Sauce Labs Onesie")

def test_login_invalid_password(page: Page):

    # Login with correct username but invalid password
    login_to_sauce_demo(page, username="standard_user", password="wrong_sauce")

    # Assertion 1: We should stay on login page (redirection to anywhere will not happen)
    expect(page).to_have_url("https://www.saucedemo.com/")

    # Assertion 2: We will see an error message containing "Username and password do not match"
    expect(page.get_by_test_id("error")).to_contain_text("Username and password do not match")

def test_login_missing_username(page: Page):

    # Try to login -> leave username blank, use correct password
    login_to_sauce_demo(page, username="", password="secret_sauce")

    # Assertion 1: We stay on a login page (no redirection)
    expect(page).to_have_url("https://www.saucedemo.com/")

    # Assertion 2: We will see an error message containing "Username is required"
    expect(page.get_by_test_id("error")).to_contain_text("Username is required")