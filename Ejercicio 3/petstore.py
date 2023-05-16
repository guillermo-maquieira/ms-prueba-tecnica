import requests
from collections import Counter

names = []

def sold_pets(r):
    data = []
    for element in r.json():
        try:
            data.append({'id': element['id'], 'name': element['name']}) 
        except KeyError:
            pass
    return data


def pet_names(name):
    names.append(name)


r = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=sold', auth=('test','abc123'))
pets = sold_pets(r)

for pet in pets:
    pet_names(pet['name'])
    print(pet, end=',')

print(Counter(names))
