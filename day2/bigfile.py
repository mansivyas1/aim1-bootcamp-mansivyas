import csv

# task6
from pathlib import Path

file_path = Path(__file__).parent / "big.txt"

with open(file_path, "w", encoding="utf-8") as f:
    for i in range(1, 500001):
        f.write("this is line {i}. python is useful")

print("file created sucessfully")

count = 0

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        count += 1

print("total lines", count)


word = "python"
matching_lines = 0

with open("big.txt", "r", encoding="utf-8") as f:
    for line in f:
        if word in line:
            matching_lines += 1

print("lines containing python", matching_lines)


with open("student.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["a", 30])
    writer.writerow(["b", 25])

with open("student.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# task8
def class_average(students, passing=40):
    total = 0
    passed = 0

    for s in students:
        total += s["marks"]  # breakpoint()

        if s["marks"] >= passing:
            passed += 1

    average = total / len(students)
    pass_rate = passed / len(students) * 100
    return average, pass_rate


data = [
    {"name": "asha", "marks": 88},
    {"name": "ravi", "marks": 92},
    {"name": "meera", "marks": 79},
    {"name": "dev", "marks": 40},
]

result = class_average(data)

print("average", result[0])
print("pass rate", result[1])
