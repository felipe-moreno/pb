import requests
from jsonschema import validate
import jsonschema

class requisicao():
    
    def __init__(self,endereco) -> None:
        self.endereco = endereco
        self.schema = {
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


    def validar_get(self):
        response = requests.get(str('{}/1'.format(self.endereco)))
        if (response.ok):
            print (response)
            print (response.text)
        else:
            print (response)
            print ('Falha na comunicação GET')
        

    def validar_post(self, json):
        response = requests.post(self.endereco, json=json)
        if (response.ok):
            print (response)
            print (response.text)
        else:
            print (response)
            print ('Falha na comunicação POST')


    def validar_put(self, json):
        response = requests.put(str('{}/3'.format(self.endereco)), json=json)
        if (response.ok):
            print (response)
            print (response.text)
        else:
            print (response)
            print ('Falha na comunicação PUT')


    def validar_delete(self):
        response = requests.delete(str('{}/1'.format(self.endereco)))
        if (response.ok):
            print (response)
            print ('Postagem 1 apagada.')
        else:
            print (response)
            print ('Falha na comunicação DELETE')


    def get_user(self):
        response = requests.get(str('{}/1'.format(self.endereco)))
        return response.json()

    def validar_json(self):
        try:
            jsonschema.validate(instance=self.get_user(), schema=self.schema)
            print ('Json ok.')
        except jsonschema.ValidationError:
            print ('Json com erro.')