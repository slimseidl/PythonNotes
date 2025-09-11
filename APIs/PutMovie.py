import requests 

r = requests.put(
    'http://127.0.0.1:5000/films/1',
    json={'name': 'Avengers: Infinity War', 'year': 2018, 'month': 'March'}
)
# puts movie into database with corresponding json object
print(r.json())

print(r.json())