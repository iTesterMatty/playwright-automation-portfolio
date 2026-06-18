import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage

# Load the environment variables from the .env file into Python's memory
load_dotenv()
# --- FIXTURES ---
# Runs automatically once before any tests start
@pytest.fixture(scope="module", autouse=True)
def configure_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(scope="module")
def credentials():
    """Provides valid application credentials securely from the environment"""
    return {
        "username": os.getenv("SAUCE_USER"),
        "password": os.getenv("SAUCE_PASSWORD")
    }

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Automatically provides an initialized LoginPage object to tests."""
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Automatically provides an initialized InventoryPage object to tests."""
    return InventoryPage(page)

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Automatically provides an initialized CartPage object to tests."""
    return CartPage(page)

@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    """Automatically provides an initialized CheckoutPage object to tests."""
    return CheckoutPage(page)

# --- TESTING DATA ----
LOGIN_DATA = [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("invalid_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
]

# --- TESTS ---

def test_login_and_shop(page: Page, login_page: LoginPage, inventory_page: InventoryPage, credentials):
    # --- ACT ---
    
    login_page.navigate()

    # Login with correct credentials
    login_page.login(credentials["username"], credentials["password"])

    # Buy a backpack item
    inventory_page.add_item_to_cart("Sauce Labs Backpack")

    # Go to shopping cart
    inventory_page.open_cart()

    # --- ASSERT ---
    # Check if we are on the Shopping cart page, and if the backpack is in our cart
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

def test_sort_product_by_price(login_page: LoginPage, inventory_page: InventoryPage, credentials):
    # --- ACT ---
    # Login with correct credentials
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])

    # Choose a Price (low to high) option from a dropdown
    inventory_page.sort_by_option("Price (low to high)")

    # --- ASSERT ---
    # Check if the first item is with the lowest price $7.99
    expect(inventory_page.first_item_name).to_have_text("Sauce Labs Onesie")

@pytest.mark.parametrize("username, password, expected_error", LOGIN_DATA)
def test_negative_login_scenarios(page: Page, login_page: LoginPage, username, password, expected_error):
    # --- ACT ---
    # Login with wrong credentials
    login_page.navigate()
    login_page.login(username, password)

    # --- ASSERT ---
    # Assertion 1: We should stay on login page (redirection to anywhere will not happen)
    expect(page).to_have_url("https://www.saucedemo.com/")

    # Assertion 2: We will see an expected error message
    expect(login_page.error_message).to_have_text(expected_error)


def test_successful_end_to_end_checkout(login_page: LoginPage, inventory_page: InventoryPage, checkout_page: CheckoutPage, cart_page: CartPage, credentials):
    
    # Navigate to a page and login
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])

    # Add the "Sauce Labs Backback" to a cart
    inventory_page.add_item_to_cart("Sauce Labs Backpack")

    # Open the cart
    inventory_page.open_cart()

    # Check if the item is in the cart and proceed to checkout
    expect(cart_page.cart_item_name).to_have_text("Sauce Labs Backpack")
    cart_page.proceed_to_checkout()

    # Fill in the information and finish the order
    checkout_page.fill_checkout_info(first_name="John", last_name="Doe", postal_code="12345")
    checkout_page.finish_checkout()

    # Check if the order was completed succesfully 
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
