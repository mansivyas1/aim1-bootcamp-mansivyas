# task3

"""math utility function for calculating averages, finding the biggest number and checking
prime numbers"""


def average(nums: list[int]) -> float:
    """return the average of a list of numbers."""
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> int | None:
    """return the biggest number, or none if the list is empty"""
    if not nums:
        return None
    return max(nums)


def is_prime(n: int) -> bool:
    """check whether a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
