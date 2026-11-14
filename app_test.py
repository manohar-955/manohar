from app import add


def test_add():
    assert add(5, 10) == 15

def test_add_two():
    assert add(2, 3) == 5
