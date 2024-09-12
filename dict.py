#imort requiered libraries
import json

#step 2:read the json file
with open('lab2\students.json') as f:
  data = json.load(f)
  
#step 3:access the data
students = data['students']

#step 4:process the data
for student in students:
  print(student['name'], student['age'], student['grades'])

#step 5:wrtie a new data into students.json file, and remain the old data
data1 = {"id":"3" ,"name": "John", "age": 30, "grades": [88, 90]}
students.append(data1)

for student in students:
  print(student['name'], student['age'], student['grades'])

# when use json.dump() to write data into json file, it will overwrite the old data