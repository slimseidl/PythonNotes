import json
 
# Create a list of dictionaries
data = []  # creating a list of dictionaries
data.append({"name":"Andre Richards","DOB":"10/10/1979"}) # dict1
data.append({"name":"Melinda Jefferson","DOB":"12/31/1979"}) #dict 2

with open('data/person.json', 'w') as outfile:   # opening the JSON file for writing 
    json.dump(data, outfile) # writes our dictionary items to the file as JSON data
 
# Print the file's contents
f = open('data/person.json', 'r')
print(f.read())
f.close()