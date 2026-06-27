import json
from playwright.sync_api import APIRequestContext

class ApiUserPage:
    def __init__(self, request: APIRequestContext):
        # Injects Playwright's request context instead of a page
        self.request = request
        self.base_url = "https://jsonplaceholder.typicode.com"

    def create_user(self, name: str, job: str):
        """Sends a POST request to create new user."""
        payload = {"name": name, "username": job}

        return self.request.post(
            f"{self.base_url}/users",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
    
    def get_user(self, user_id: int):
        """Sends a GET request to fetch a specific user."""
        response = self.request.get(f"{self.base_url}/users/{user_id}")
        return response