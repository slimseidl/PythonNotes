import requests 

data = requests.get('http://127.0.0.1:5000/')
# with APIs.py running 
print(type(data))
# returns <class 'requests.models.Response'>
print(data.json())
# returns response 200 (reached endpoint) 

# With API open, shows that a request was made 127.0.0.1 - - [10/Sep/2025 16:28:02] "GET / HTTP/1.1" 200 -