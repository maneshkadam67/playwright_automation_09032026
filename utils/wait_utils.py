def wait_for_element(page, locator, timeout=5000):
    page.wait_for_selector(locator, timeout=timeout)