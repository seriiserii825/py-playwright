from modules.async_playwright_api import async_playwright_api
from modules.sync_playwright_api import sync_playwright_api


def main():
    print("Hello, World!")
    # sync_playwright_api()
    async_playwright_api()


if __name__ == "__main__":
    main()
