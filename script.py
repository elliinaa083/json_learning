import json

file = open('students.json')
data = json.load(file)
age = 0


human = len(data['Students'])
for student in data['Students']:
    age += int(student['Age'])

print( age / human)