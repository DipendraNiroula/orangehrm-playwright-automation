import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        headless = bool(os.getenv("CI", False))
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        context.set_default_timeout(60000)  # 60 seconds
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )
        page = context.new_page()
        yield page
        context.tracing.stop(path="trace.zip")
        browser.close()