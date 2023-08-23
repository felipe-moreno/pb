def json_schema():
    return ({
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
})

def postagem():
    return ({
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

def postagem_alterada():
    return ({
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
}
)