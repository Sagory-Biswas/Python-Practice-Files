#dictionarys:

StudentInfo = {
    "student1": {
    "name": "Saikat Sarker",
    "grade" : "11th",
     "roll": 10,
     "Id No": 123450
    },

    "student2": {
    "name": "Surjo Sarker",
    "class": "10",
     "roll": 11,
     "Id No": 123460
    },

    "student3":{
     "name": "Sourav sarker",
    "class": "10th",
     "roll": {
         "claas roll": 13,
         "exam roll": 4103
     },

     "Id No": 123470
    }
}

print(StudentInfo)
print(StudentInfo["student1"])
print(StudentInfo["student3"]["roll"]["exam roll"])

#Dictionaries Access:

print(StudentInfo.get("student1"))
print(StudentInfo.keys())
print(StudentInfo.values())

#Changes Values:

'''StudentInfo["student3"] = "None"
print(StudentInfo)

StudentInfo.update({"student1":"absent"})
print(StudentInfo)
'''
#Remove Items:

'''StudentInfo.pop("student1")
print(StudentInfo)

StudentInfo.popitem()
print(StudentInfo)'''

'''del StudentInfo["student2"]
print(StudentInfo)

StudentInfo.clear()
print(StudentInfo)'''

#Loop Items:

print(StudentInfo)

for a in StudentInfo:
    print(a)
for b in StudentInfo.values():
    print(b)

for c in StudentInfo.keys():
    print(c)

for d in StudentInfo.items():
    print(d)

#Copy Dictionaries:

print(StudentInfo)

x = StudentInfo.copy()
print(x)

y = dict(StudentInfo)
print(y)

print(len(StudentInfo))
print(type(StudentInfo))