# task1
from mathutils import average, biggest, is_prime


def test_average():
    assert average([10, 20, 30]) == 20
    assert average([5, 15]) == 10


def test_biggest():
    assert biggest([10, 50, 30]) == 50
    assert biggest([50, 80, 90]) == 90


def test_is_prime():
    assert is_prime(7)
    assert is_prime(10)


def test_average_happy_path():
    assert average([10, 20, 30]) == 20
    assert average([5, 15]) == 10


def test_average_edge_cases():
    assert average([]) == 0
    assert average([10]) == 10
    assert average([0, 0]) == 0
    assert average([-5, -15]) == -10


def test_biggest_happy_path():
    assert biggest([10, 50, 30]) == 50
    assert biggest([50, 80, 90]) == 90


def test_biggest_edge_cases():
    assert biggest([7]) == 7
    assert biggest([0, -5]) == 0
    assert biggest([-10, -3, -8]) == -3


def test_is_prime_happy_path():
    assert is_prime(7)
    assert is_prime(10)


def test_is_prime_edge_cases():
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(-5)
    assert is_prime(2)
