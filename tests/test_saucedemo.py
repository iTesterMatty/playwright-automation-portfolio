from playwright.sync_api import Page, expect

# def test_login_and_shop(page: Page):

#     # --- ARRANGE ---
#     page.goto("https://www.saucedemo.com/")

#     # --- ACT ---
#     # Login 
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")
#     page.get_by_role("button", name="Login").click()

#     # Buy a backpack item
#     item = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
#     item.get_by_role("button", name="Add to cart").click()

#     # Go to shopping cart
#     page.locator(".shopping_cart_link").click()

#     # --- ASSERT ---
#     # Check if we are on the Shopping cart page, and if the backpack is in our cart
#     expect(page).to_have_url("https://www.saucedemo.com/cart.html")
#     expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

def test_sort_product_by_price(page: Page):

    # --- ARRANGE ---
    page.goto("https://www.saucedemo.com/")

    # --- ACT ---
    # Login 
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Choose a Price (low to high) option from a dropdown
    page.get_by_role("combobox").select_option(label="Price (low to high)")

    # --- ASSERT ---
    # Check if the first item is with the lowest price $7.99
    expect(page.locator(".inventory_item_name").first).to_have_text("Sauce Labs Onesie")