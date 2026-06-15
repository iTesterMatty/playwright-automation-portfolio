from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.cart_item_name = page.locator(".inventory_item_name")

    def proceed_to_checkout(self):
        """Clicks the checkout button to the information form."""
        self.checkout_button.click()