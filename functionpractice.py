for i in range(1, 100):
    if i % 15 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    elif i % 7 == 0: print("Bazz")
    else: print(i)

string = "the cat sat" 
reversed_string = string[:: -1]
words = reversed_string.split()
print(words)

string = "the cat sat"
count_a = string.count("t")
print(count_a)

number = [1, 2, 3, 4, 5, 6, 7, 8]
result = [x*2 for x in number if x % 2 == 0]
print(result)

number = [5, 2, 3, 8, 2, 1, 4, 6, 7]
unique_numbers = sorted(set(number))
print(unique_numbers)

def is_paildrome(word): 
    if word == word[:: -1]: 
        return (True)
    else: 
        return(False)
print(is_paildrome("madam"))
print(is_paildrome("hello"))

from typing import Dict, List, Union 
def calculate_stats(numbers: List[Union[int, float]]) -> Dict[str, Union[int, float, str]]:
    """calculates the min, max and count of a list of numbers."""
    if not numbers: 
        return {"error": "empty list"}
    return {"min": min(numbers), 
            "max": max(numbers),
            "mean":sum(numbers)/len(numbers),
            "count":len(numbers)
            }
def safe_divide(a: float, b:float) -> Union[float, str]:
    """saafely divides two numbers and handles division by zero"""
    try: 
        return a / b
    except ZeroDivisionError:
        return "error: division by zero is not allowed"
