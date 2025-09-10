import requests

# getting all films from movie DB
req = requests.get('http://127.0.0.1:5000/films')
print(req.json())
# Getting film ID 1
r = requests.get('http://127.0.0.1:5000/films/1')
print(r.json())

