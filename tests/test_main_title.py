from playwright.sync_api import Page


def test_main_title(page: Page):
    page.goto("https://iteco.altuofianco.com/")
    assert page.title() == "ITECO - Home"
