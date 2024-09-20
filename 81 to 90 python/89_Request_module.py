# request model

import requests
# responce = requests.get("https://ayaz-website.netlify.app/")
# print(responce.text)

# upper 3 line of code give us pure html code

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title":"ayaz",
    "body":"bhai",
    "userId":1
}
headers = {
    "Content-type":"application/json;charset=UTF-8"
}
responce = requests.post(url,headers=headers, json=data)
print(responce.text)