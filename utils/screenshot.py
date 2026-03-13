# import pytest
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call" and rep.failed:
#         page = item.funcargs["page"]
#         page.screenshot(path="screenshots/failure.png")


import os

def capture_screenshot(page, name):

    os.makedirs("screenshots", exist_ok=True)

    path = f"screenshots/{name}.png"
    page.screenshot(path=path)