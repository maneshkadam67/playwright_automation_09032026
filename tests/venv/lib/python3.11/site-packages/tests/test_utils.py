# tests/test_utils.py
#from db_helper.utils import assert_equal
import pytest
from db_row_helper.db_helper.utils import assert_equal


def test_assert_equal_pass():
    assert assert_equal(5, 5)

def test_assert_equal_fail():
    with pytest.raises(AssertionError):
        assert_equal(5, 3, "Row count mismatch")
