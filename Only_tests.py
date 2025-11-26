import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_footer_check(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")
    footer = page.locator("footer")

"""проверка наличия футера"""

def test_buttin_new_project(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")
    page.locator("footer").get_by_role("button", name="Начать проект").click()

"""проверка кнопки начать проект"""

def test_button_be(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="be").click()
        page1 = page1_info.value

"""проверкаькнопки dp"""

def test_button_dp(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="dp").click()
    page1 = page1_info.value

"""проверка кнопки vk"""

def test_button_vk(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="vk", exact=True).click()
    page1 = page1_info.value


    # ---------------------
    context.close()
    browser.close()

