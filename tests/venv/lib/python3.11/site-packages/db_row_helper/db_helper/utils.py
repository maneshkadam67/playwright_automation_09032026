
def assert_equal(actual, expected, message=""):
    if actual != expected:
        raise AssertionError(f"{message} Expected {expected}, got {actual}")
    return True
