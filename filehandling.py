import csv
import json
#1. Context Managers (with)
with open("data.txt", "r") as file:
    content = file.read()
# file is automatically closed here



#2. CSV (Comma-Separated Values)
#Reading
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # each row is a list

#Writing
data = [["Name", "Age"], ["Bipin", 22], ["Rita", 25]]
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

#DictReader / DictWriter
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])

#3. JSON (JavaScript Object Notation)
#Reading
with open("data.json", "r") as f:
    data = json.load(f)   # dict
print(data)

#Writing
person = {"name": "Bipin", "age": 22, "skills": ["Python", "ML"]}

with open("data.json", "w") as f:
    json.dump(person, f, indent=4)  # pretty print

#Converting String ↔ Python
json_string = '{"x": 5, "y": 10}'
data = json.loads(json_string)   # str → dict
print(data["x"])

python_obj = {"x": 5, "y": 10}
json_str = json.dumps(python_obj)   # dict → str
print(json_str)