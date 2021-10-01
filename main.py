def sum_of_squares(a):
    return sum([x ** 2 for x in a])


def test_one():
    assert sum_of_squares([1, 2, 3]) == 14


def test_two():
    assert ([1, 2, 3, 4, 5]) == 55


if __name__ == '__main__':
    test_one()
    test_two()
