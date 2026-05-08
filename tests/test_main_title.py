from playwright.sync_api import Page


def test_main_title(page: Page):
    title = "Iteco Srl | La tua flotta merita un sistema di lavaggio che duri nel tempo"
    page.goto("https://iteco.altuofianco.com/")
    assert page.title() == title
