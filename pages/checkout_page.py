from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # Information form locators
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="continue")

        # Overview and finish locators
        self.finish_button = page.get_by_role("button", name="Finish")
        self.complete_header = page.locator(".complete-header")
    
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """Fills out the shipping information and proceeds."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()
    
    def finish_checkout(self):
        """Clicks he final confirmation finish button."""
        self.finish_button.click()