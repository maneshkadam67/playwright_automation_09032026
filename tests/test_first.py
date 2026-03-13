import time

from pages.first_page import FirstPage

# def test_first(page:Page):
#     # browser=playwright.chromium.launch(headless=False)
#     # context=browser.new_context()
#     # page=context.new_page()
#
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill("standard_user")
#     page.fill("#password","secret_sauce")
#     page.click("#login-button")



def test_first(page):
    loginpage=FirstPage(page)
    loginpage.open_login_page()
    loginpage.login("standard_user","secret_sauce")
    time.sleep(4)

# def test_first():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)
#         page=browser.new_page()
#         page.goto("https://www.saucedemo.com/")
#         time.sleep(4)
#         page.fill("#user-name","standard_user")
#         page.fill("#password","secret_sauce")
#         page.click("#login-button")
#         time.sleep(3)
#         browser.close()