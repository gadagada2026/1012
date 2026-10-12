"""Shared pytest fixtures for UI tests (Playwright)."""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """Session-scoped Playwright browser instance."""
    with sync_playwright() as p:
        # headless=True 默认无头运行；调试时加 --headed 更直观
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    """Function-scoped page: 每个测试一个独立页面，互不干扰."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
