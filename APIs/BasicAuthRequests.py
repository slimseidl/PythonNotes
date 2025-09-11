import requests 

# Doesn't work, status code 400, no auth
r = requests.get('http://127.0.0.1:5000/hello_world')
print(r.status_code)


# this one works and returns the 200 code and json 
r = requests.get('http://127.0.0.1:5000/hello_world', auth =('admin', 'atch_5K}?g'))
print(r.status_code)
print(r.json())



