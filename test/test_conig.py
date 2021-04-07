import pytest

class NotInRangeError(Exception):
    def __init__(self, message="value is not in accepatable range!!"):
        self.message = message
        super().__init__(self.message)



def test_generic():
    a = 2
    with pytest.raises(NotInRangeError):
        if a not in range(10,20):
            raise NotInRangeError

def test_something():
    a=2
    b=2
    assert True