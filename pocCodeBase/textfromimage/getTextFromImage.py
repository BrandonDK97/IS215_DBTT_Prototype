import json
import base64
from urllib import request
import requests
import json


data = {}
with open("Screenshot 2022-03-26 201627.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    print(encoded_string)
    data["image"] = encoded_string.decode("utf-8")

jsonData = json.dumps(data)

url = 'e'

req = requests.post(url,headers={"x-api-key": "", "Content-Type": "application/json"} ,json=jsonData)

print(req)