import requests
from jsonschema import validate
import jsonschema

def validar_json(json_retorno):
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "suite": {"type": "string"},
                    "city": {"type": "string"},
                    "zipcode": {"type": "string"},
                    "geo": {
                        "type": "object",
                        "properties": {
                            "lat": {"type": "string"},
                            "lng": {"type": "string"},
                        }
                    }
                }
            },
            "phone": {"type": "string"},
            "website": {"type": "string"},
            "company": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "catchPhrase": {"type": "string"},
                    "bs": {"type": "string"},
                }
            },
        },
    }

    try:
        jsonschema.validate(instance=json_retorno, schema=schema)
        print("Json ok.")
    except jsonschema.ValidationError as e:
        print("Json com erro, validar.")


response1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
response2 = requests.post("https://jsonplaceholder.typicode.com/users", json={
    "id": 3,
    "name": "Felipe Moreno",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
})
print(response2.json())

response3 = requests.put("https://jsonplaceholder.typicode.com/users/3", json={
    "id": 3,
    "name": "Felipe Moreno Lorente Lopes",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
})
print(response3.json())

response4 = requests.delete("https://jsonplaceholder.typicode.com/users/1")

validar_json(response1.json())

if (response1.ok and response2.ok and response3.ok and response4.ok):
    print("Retorno 200, ok.")
else:
    print("Retorno diferente de 200, verificar.")
