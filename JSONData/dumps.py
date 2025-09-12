import json
 
json_dict = {    "first_name": "Robert",
    "last_name": "Balti",
    "role": ["Manager", "Lead Developer"],
    "age": 34
} # python dictionary 
 
# convert a dictionary into a string object that we can display. 
json_data = json.dumps(json_dict)  # Optional indent parameter to output every item on a separate line 
# json_data = json.dumps(json_dict, indent=4) 4 spaces for the indent
 
print(json_dict)       # dict
print(type(json_dict))
 
print(json_data)       # string
print(type(json_data))


# Below is output without indent 
#{'first_name': 'Robert', 'last_name': 'Balti', 'role': ['Manager', 'Lead Developer'], 'age': 34}
#<class 'dict'>
#{"first_name": "Robert", "last_name": "Balti", "role": ["Manager", "Lead Developer"], "age": 34}
#<class 'str'>

#ouput with indent param

#{
#   "first_name": "Robert",
#    "last_name": "Balti",
#    "role": [
#        "Manager",
#        "Lead Developer"
#    ],
#    "age": 34
#}
# <class 'str'>