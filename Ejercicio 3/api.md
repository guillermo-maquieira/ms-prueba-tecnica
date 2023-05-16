# Tratamiento de datos en APIs

1. En una primera interacción con la API y utilizando la api key `special-key` se obtiene la siguiente información:

> "Right now we have one user in our system: test, with password: abc123"

2. Se procede a consultar el endpoint `findByStatus` solicitado cuyo estado sea `vendido`:

```shell
curl -X 'GET' 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold' -H 'accept: application/json'
```

3. Se obtiene la siguiente respuesta (abreviada a fines ilustrativos) por línea de comandos:

```json
[{
    "id": 9223372036854775096,
    "category": {
        "id": 0,
        "name": "someCategory"
    },
    "name": "Captain Chewie",
    "photoUrls": ["http://mypetphotos.com/chewie"],
    "tags": [{
        "id": 0,
        "name": "someTag"
    }],
    "status": "sold"
}, {
    "id": 9223372036854775100,
    "category": {
        "id": 0,
        "name": "someCategory"
    },
    "name": "Captain Corky",
    "photoUrls": ["http://mypetphotos.com/corky"],
    "tags": [{
        "id": 0,
        "name": "someTag"
    }],
    "status": "sold"
}, {
    "id": 9223372036854775102,
    "category": {
        "id": 0,
        "name": "someCategory"
    },
    "name": "Captain Patches",
    "photoUrls": ["http://mypetphotos.com/patches"],
    "tags": [{
        "id": 0,
        "name": "someTag"
    }],
    "status": "sold"
}, {
    "id": 9223372036854775103,
    "category": {
        "id": 0,
        "name": "someCategory"
    },
    "name": "Captain Ike",
    "photoUrls": ["http://mypetphotos.com/ike"],
    "tags": [{
        "id": 0,
        "name": "someTag"
    }],
    "status": "sold"
}, {
    "id": 9223372036854775104,
    "category": {
        "id": 0,
        "name": "someCategory"
    },
    "name": "Captain Corky",
    "photoUrls": ["http://mypetphotos.com/corky"],
    "tags": [{
        "id": 0,
        "name": "someTag"
    }],
    "status": "sold"
}, {
    "id": 9223372036854775105,
    "category": {
        "id": 0,
        "name": "someCategory"
    },
    "name": "Captain Skip",
    "photoUrls": ["http://mypetphotos.com/skip"],
    "tags": [{
        "id": 0,
        "name": "someTag"
    }],
    "status": "sold"
}, {
    "id": 9223372036854775106,
    "category": {
        "id": 0,
        "name": "someCategory"
    },
    "name": "Captain Chewie",
    "photoUrls": ["http://mypetphotos.com/chewie"],
    "tags": [{
        "id": 0,
        "name": "someTag"
    }],
    "status": "sold"
}]
```