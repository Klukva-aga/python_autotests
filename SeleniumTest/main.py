import requests

# Создание питомца
response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 501,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "kosha",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)


# Смена имени питомца
response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 501,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "kokosha",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

# Нахождение пета по ID
response = requests.get("https://petstore.swagger.io/v2/pet/501")
print(response.text)