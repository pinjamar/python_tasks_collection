
# Python program to convert
# Python to JSON
    
    
# import json
    
# # Data to be written
# dictionary ={
#   "id": "04",
#   "name": "sunil",
#   "department": "HR"
# }
# print(type(dictionary))
# # Serializing json 
# json_object = json.dumps(dictionary, indent = 4)
# print(type(json_object))

import json
  
# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

