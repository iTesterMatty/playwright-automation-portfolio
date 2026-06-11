from playwright.sync_api import Page, expect

def test_add_todo(page: Page):
    
    # --- ARRANGE ---
    page.goto("https://demo.playwright.dev/todomvc")

    # --- ACT ---
    todo_input = page.get_by_placeholder("What needs to be done?")
    todo_input.fill("Write some more tests")
    todo_input.press("Enter")

    # --- ASSERT ---
    expect(page.get_by_text("Write some more tests")).to_be_visible()

def test_todo_lifecycle(page: Page):

    # --- ARRANGE ---
    page.goto("https://demo.playwright.dev/todomvc")
    todo_input = page.get_by_placeholder("What needs to be done?")

    # --- ACT ---
    # Enter two tasks to be done
    todo_input.fill("Buy Milk")
    todo_input.press("Enter")

    todo_input.fill("Clean the kitchen")
    todo_input.press("Enter")

    # Check off one of them to complete it
    page.locator("li").filter(has_text="Buy Milk").get_by_role("checkbox").check()

    # Change filter to active tasks (not done yet)
    page.get_by_role("link", name="Active").click()

    # --- ASSERT ---
    expect(page.get_by_text("Buy Milk")).to_be_hidden()
    expect(page.get_by_text("Clean the kitchen")).to_be_visible()

def test_delete_todo(page: Page):
    
    # --- ARRANGE ---
    page.goto("https://demo.playwright.dev/todomvc")
    todo_input = page.get_by_placeholder("What needs to be done?")

    # --- ACT ---
    # Enter three tasks
    todo_input.fill("Task Alpha")
    todo_input.press("Enter")

    todo_input.fill("Task Beta")
    todo_input.press("Enter")

    todo_input.fill("Task Gamma")
    todo_input.press("Enter")

    # Delete "Task Beta"
    beta_row = page.locator("li").filter(has_text="Task Beta")
    beta_row.hover()
    beta_row.get_by_role("button", name="Delete").click()

    # --- ASSERT ---
    expect(page.get_by_text("Task Alpha")).to_be_visible()
    expect(page.get_by_text("Task Gamma")).to_be_visible()
    expect(page.get_by_text("Task Beta")).to_be_hidden()