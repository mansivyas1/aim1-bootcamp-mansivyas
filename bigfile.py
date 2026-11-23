"""with open("big.txt", "w",encoding="utf-8") as f:
    for i in range(1, 500001):
        f.write("this is line {i}. python is useful")

print("file created sucessfully")

count = 0

with open("big.txt", "r",encoding="uft-8") as f:
    for line in f:
        count += 1 
        
print("total lines", count)


word = "python"
matching_lines = 0

with open("big.txt", "r", encoding="utf-8") as f :
    for line in f:
        if word in line:
            matching_lines += 1

print("lines containing python", matching_lines)

import csv 

with open("student.csv" , "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["a", 30])
    writer.writerow(["b", 25])

with open("student.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)"""


def class_average(students, passing=40):
    total = 0
    passed = 0
    for s in students:
        total = s["marks"]
        if s["marks"] > passing:
            passed += 1
    average = total / len(students)
    pass_rate = passed / len(students) * 100
    return average, pass_rate
 
data = [
    {"name": "asha",  "marks": 88},
    {"name": "ravi",  "marks": 92},
    {"name": "meera", "marks": 79},
    {"name": "dev",   "marks": 40},
]
avg, rate = class_average(data)
print(f"average: {avg}")      # prints 10.0
print(f"pass rate: {rate}%")  # prints 75.0
