import re
from collections import Counter

text = """
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these"""

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails = re.findall(email_pattern, text)
print("email addresses")
print(emails)
print("total emails", len(emails))

phone_pattern = r'\+91\s?\d{5}\s?\d{5}|\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print("phone numbers")
print(phones)

email_pattern_groups = r'([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})'
email_details = re.findall(email_pattern_groups, text)
print("username and domin")
for username, domin in email_details:
    print("username", username)
    print("domin",domin)

domins = [domin.lower() for username, domin in email_details]

domin_count = Counter(domins)

print("email count by domin")
print(domin_count)

"""employees = {}
employees["it"].append("rahul")"""

from collections import defaultdict

data = [("it", "rahul"),
        ("hr", "priya"),
        ("sales", "neha"),
        ("hr", "karan"),
        ("it", "ravi")]

employees = defaultdict(list)

for department, employee in data:
    employees[department].append(employee)

print(dict(employees))

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])

people = [("rahul", 22, "ahemdabad"),
          ("priya", 24, "surat"),
          ("amit", 23, "gandhinagar"),
          ("neha", 25, "gadhinagar")]

people_named = [Person(*person) for person in people]
print("all people")
for person in people_named:
    print(person)

print("accessing values by name")
for person in people_named:
    print("name", person.name)
    print("age", person.age)
    print("city", person.city)

p = people_named[0]

print("using index", p[2])
print("using name", p.city)

from collections import deque

search_history = deque(maxlen=5)
searches = ["python", " java", "css", "js", "html", "sql"]
for search in searches:
    search_history.append(search)
    print("new search", search)
    print("search history", list(search_history))
print("final last 5 searches")
print(list(search_history))

from collections import Counter
text1 = "python is easy and python is powerful"
text2 = "python is popular and java is powerful"

words1 = text1.lower().split()
words2 = text2.lower().split()

count1 = Counter(words1)
count2 = Counter(words2)

print("text 1 word counts", count1)
print("text 2 word counts", count2)

common_words = count1.keys() & count2.keys()
print("common words are")
print(common_words)

only_words = count1.keys() - count2.keys()
print("word only in text1")
print(only_words)

only_words = count2.keys() - count1.keys()
print("words only in text2")
print(only_words)

import random 
from datetime import datetime, timedelta

levels = ["INFO", "WARN", "ERROR"]

messages = {
    "INFO": ["Application started",
             "User logged in",
             "File uploaded succesfully",
             "Data processed successfully",
             "User looed out"],
    "WARN": ["Memory usage is high",
             "Slow network connection",
             "Disk space is low",
             "Invalid input detected"],
    "ERROR": ["Database connection failed",
              "file not found",
              "Payment processing failed",
              "Authentication failed"]}
start_time = datetime(2026, 11, 23, 8, 0, 0)

with open("app.log","w", encoding="utf-8") as file:
    for i in range(250):
        timestamp = start_time + timedelta(minutes=i)

    level = random.choice(levels)
    message = random.choice(messages[level])

    log_line = (f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
            f"{level} {message}\n")

    file.write(log_line)

print("log file generated successfully")

with open("app.log", "r", encoding="utf-8") as file:
    lines = file.readline()

print("total line", len(lines))

print("testing loop")
for i in range(250):
    pass

print("loop count", i + 1)

with open("app.log", "r", encoding="utf-8") as file:
    content = file.read()

print("total newline characters", content.count("\n"))
print("total file characters", len(content))

import re

pattern = r"(/d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARN|ERROR) (.+)"

entries = []

with open("app.log", "r", encoding="utf-8") as file:
    for line in file:
        match = re.match(pattern, line.strip())
        if match:
            timestamp_str = match.group(1)
            level = match.group(2)
            message = match.group(3)
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%D %H:%M:%S")
            entries.append({"timestamp": timestamp,
                            "level": level,
                            "message": message})

print("total parsed entries", len(entries))
print("first 5 parsed entries")

for entry in entries[:5]:
    print(entry)

level_counts = Counter(entry["level"] for entry in entries)
print("log level counts")

for level, count in level_counts.items():
    print(level, ":", count)

hour_counts = Counter(entry["timestamp"].hour for entry in entries)
print("hourly log counts")

for hour,count in sorted(hour_counts.items()):
    print("{hour}:00 - {count}entries")

busiest_hour = hour_counts.most_common(1)
print("busiest hour", busiest_hour)

logs_by_level = defaultdict(list)
for entry in entries:
    logs_by_level[entry["level"]].append(entry)

print("logs grouped by level")
for level, logs in logs_by_level.items():
    print("{level}:")
    for log in logs[:3]:
        print(log["timestamp"], "-", log["message"])
        print("total entries", len(logs))

error_entries = [entry for entry in entries if entry["level"] == "ERROR"]
error_entries.sort(key=lambda x: x["timestamp"])
longest_gap = timedelta(0)
for i in range(1, len(error_entries)):
    gap = (error_entries[i]["timestamp"] - error_entries[i - 1]["timestamp"])
    if gap > longest_gap:
        longest_gap = gap
print("error analysis")
print("total error entries", len(error_entries))
if len(error_entries) >= 2:
    print("lonest gap between errors", longest_gap)
else:
    print("not enough error entries to calculate the gap")
