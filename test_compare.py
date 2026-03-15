import pytest


@pytest.mark.hi
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.hi
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.ot
def test_less():
   num = 100
   assert num < 200