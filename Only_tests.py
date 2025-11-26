import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


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

    # проверка наличия футера
    expect(footer).to_be_visible()
    assert footer.count() > 0, "Футер не найден"

    context.close()
    browser.close()


def test_buttin_new_project(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")

    # проверка кнопки начать проект
    button = page.locator("footer").get_by_role("button", name="Начать проект")
    expect(button).to_be_visible()
    button.click()

    context.close()
    browser.close()


def test_button_be(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")

    # проверка кнопки be
    be_link = page.get_by_role("link", name="be")
    expect(be_link).to_be_visible()

    with page.expect_popup() as page1_info:
        be_link.click()
    page1 = page1_info.value

    page1.close()
    context.close()
    browser.close()


def test_button_dp(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")

    # проверка кнопки dp
    dp_link = page.get_by_role("link", name="dp")
    expect(dp_link).to_be_visible()

    with page.expect_popup() as page1_info:
        dp_link.click()
    page1 = page1_info.value

    page1.close()
    context.close()
    browser.close()


def test_button_vk(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://only.digital/")

    # проверка кнопки vk
    vk_link = page.get_by_role("link", name="vk", exact=True)
    expect(vk_link).to_be_visible()

    with page.expect_popup() as page1_info:
        vk_link.click()
    page1 = page1_info.value

    page1.close()
    context.close()
    browser.close()

