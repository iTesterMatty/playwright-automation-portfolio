import base64
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hooks into test execution reports to attach media assets on test failures."""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.failed and not xfail) or (report.skipped and xfail):
            if 'page' in item.funcargs:
                page = item.funcargs['page']
                
                # 1. Capture the screenshot as raw binary bytes
                screenshot_bytes = page.screenshot(type="png", full_page=True)
                
                # 2. Convert the raw bytes into a safe Base64 encoded string format
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
                
                # 3. Embed the safe string into the HTML structure
                extra.append(pytest_html.extras.image(screenshot_base64, 'Failure Screenshot'))
        report.extras = extra