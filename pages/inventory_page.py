from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # We store the explicit selectors right inside the POM 
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.get_by_role("combobox")
        self.first_item_name = page.locator(".inventory_item_name").first
    
    def add_item_to_cart(self, item_name: str):
        """Filters catalog items by name and clicks its Add to cart button"""
        item = self.page.locator(".inventory_item").filter(has_text=item_name)
        item.get_by_role("button", name="Add to cart").click()
    
    def sort_by_option(self, option_label: str):
        """Selects a sorting rule from the dropdown selection box."""
        self.sort_dropdown.select_option(label=option_label)
    
    def open_cart(self):
        """Navigates diretcly to the shoppin cart view."""
        self.cart_link.click()