numbers = [1, 2, 3, 4, 5]
out = []
for n in numbers:
    if n % 2 == 1:
        out.append(n * n)

print(out)

names = ["a", "B", "c", "d", "E"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

from itertools import pairwise

list1 = [10, 50, 30, 80, 55]
list2 = [60, 20, 40, 70, 90]
products = [a * b for a, b in zip(list1, list2)]
print(products)

sentences = ["hello", "short text", "learning python", "coding in python is fun"]
for text in sentences:
    if len(text.split()) > 4:
        print(text)

from functools import reduce

numbers = [2, 3, 4, 5,]
products = reduce(lambda x, y: x * y, numbers)
print(products)

items = [
    {"name" : "books", "price" : 250},
    {"name" : "notebook", "price" : 100}]

total_price =  sum(item.get("price", 0) for item in items)
print(total_price)

nested_list = [[1,2], [3,4], [5,6]]
flat = [item for sublist in nested_list for item in sublist]
print(flat)

words = ["apple", "banana", "cheery"]
length_map = {s: len(s) for s in words}
print(length_map)

items = [0, "apple", "banana", [], 50, "", None]
truthy_item = [x for x in items if x]
print(truthy_item)
falsy_item = [x for x in items if not x ]
print(falsy_item)

from itertools import accumulate 
numbers = [1, 2, 3]
running_total = list(accumulate(numbers))
print(running_total)

import string

"""with open("text.txt", "r", encoding="utf-8") as file: 
    text = file.read()

text = text.lower()

for punct in string.punctuation:
    text = text.replace(punct, "")

words = text.split()

count = {}

for word in words: 
    count[word] = count.get(word, 0) + 1

print(count)"""

"""from collections import Counter

with open("text.txt") as f:
    text = f.read().lower()

words = text.split()
counts = Counter(words)
print(counts.most_common(10))"""

from itertools import combinations, permutations, product

students = ["asha", "ravi", "meera", "dev", "priya"]

pairs = list(combinations(students, 2))

print("all possible pairs")
print(pairs)

print("total pairs", len(pairs))

print("combination formula result", 10)

ordered_pairs = list(permutations(students, 2))
print("all ordered pairs")
print(ordered_pairs)
print("total ordered pairs", len(ordered_pairs))

colours = ["red", "white", "blue"]
sizes = ["s", "m"]

shirt_combinations = list(product(colours, sizes))
print("shirt combinations")
print(shirt_combinations)
print("total shirt combinations", len(shirt_combinations))

features = ["age", "salary", "experience", "education"]
all_subsets = []

for r in range(len(features) +1):
    all_subsets.extend(combinations(features, r))

print("all possible feature subsets")
for subset in all_subsets: 
    print(subset)
print("total subset:", len(all_subsets))

import re 
from collections import Counter 
