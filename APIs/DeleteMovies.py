import requests 

r = requests.delete('http://127.0.0.1:5000/films/1')
# deletes film ID 1 

print(r.text)
# returns nothing since we deleted
print(r.status_code)
# returns 204

