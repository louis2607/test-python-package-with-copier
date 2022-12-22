from test_python_package_with_copier.main import add, sub


def test_add():
    assert add(1, 1) == 2


def test_sub():
    assert sub(3, 1) == 2
