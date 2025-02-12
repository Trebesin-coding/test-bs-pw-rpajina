from playwright.sync_api import sync_playwright
import os




def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://js-trebesin.github.io/playwright-exam/")

        page.fill('input[id="login"]', "Jarmil")
        page.fill('input[id="pass"]', "Admin123")

        # !!!
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!

        page.click('button[class="login-btn"]')
        page.wait_for_timeout(500)


        scrt_txt = page.get_by_text("42")
        print(scrt_txt)

        input("zavrit")

        browser.close()
    

if __name__ == "__main__":
    main()
