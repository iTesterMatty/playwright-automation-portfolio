import os
from dotenv import load_dotenv
from playwright.sync_api import Page

# Load the environment variables from the .env file into Python's memory
load_dotenv()

class LoginPage:
    def __init__(self, page: Page):
        # Pass the Playwright page instance into the class
        self.page = page

        # Define all locators for this page in one place
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_test_id("error")
    
    def navigate(self):
        """Navigates to the base URL provided by the environment configuration"""
        # os.getenv() reads the value of BASE_URL from .env file
        base_url = os.getenv("BASE_URL")
        self.page.goto(base_url)
    
    def login(self, username: str, password: str):
        """Performs the complete login action sequence"""
        # If username is empty, we skip typing to test the negative path
        if username is not None:
            self.username_input.fill(username)
        if password is not None:
            self.password_input.fill(password)
        
        self.login_button.click()