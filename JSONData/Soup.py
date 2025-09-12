import requests 
from bs4 import BeautifulSoup
url = "url"

r = requests.get(url)
response_text = r.text 
soup = BeautifulSoup(response_text,"html.parser") 

# Transforms the html to a format to access the elements 

text = '<b class="boldest">This is bold</b>'
soup = BeautifulSoup(text, "html.parser")
print(soup) 
# Result = <b class="boldest">This is bold</b>

tag = soup.b 
print(tag)
# <b class="boldest">This is bold</b>



