
from playwright.sync_api import Page, expect, Playwright
from playwright.sync_api._generated import ElementHandle

def test_example(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    locator: ElementHandle | None = page.query_selector("#L2AGLb")
    locator.click()
    expect(page.get_by_role("img", name="Google")).to_be_visible()
