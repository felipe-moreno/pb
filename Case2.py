import requests
from jsonschema import validate

response1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
response2 = requests.post("https://jsonplaceholder.typicode.com/users")
response3 = requests.put("https://jsonplaceholder.typicode.com/users/1")
response4 = requests.delete("https://jsonplaceholder.typicode.com/users/1")

schema = {
    "type": "object"

}

print(response1.json())

print (response1.status_code)
print (response2.status_code)
print (response3.status_code)
print (response4.status_code)