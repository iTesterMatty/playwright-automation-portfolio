import pytest
from playwright.sync_api import playwright, expect
from pages.api_user_page import ApiUserPage

@pytest.fixture
def api_user(playwright):
    """Fixture to initialize our API Page Object"""
    # Create an isolated API request context
    request_context = playwright.request.new_context()
    yield ApiUserPage(request_context)
    # Clean up and dispose of the context after the test finishes
    request_context.dispose()

# --- API TESTS ---

def test_create_user_successfully(api_user: ApiUserPage):
    
    # --- ACT ---
    response = api_user.create_user(name="QA Engineer", job="Automation")

    # --- ASSERT ---
    # 1. Verify that HTTP Status code is 201 (created)
    assert response.status == 201

    # 2. Parse JSON response body
    response_body = response.json()

    # 3. Verify the payload data matches what we sent
    assert response_body["name"] =="QA Engineer"
    assert response_body["username"] == "Automation"
    assert "id" in response_body # Ensures the API generated a User ID

def test_get_existing_user(api_user: ApiUserPage):

    # --- ACT ---
    # Fetching user with ID 1 (Leanne Graham - a default user in jsonplaceholder)
    response = api_user.get_user(1)

    # --- ASSERT ---
    # Verify HTTP status code is 200 (ok)
    assert response.status == 200

    response_body = response.json()

    # Verify the specific user detail returned by the API
    assert response_body["id"] == 1
    assert "email" in response_body
    assert response_body["name"] == "Leanne Graham"



