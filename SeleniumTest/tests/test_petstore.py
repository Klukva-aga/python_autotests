import requests
import pytest

# Проверка, что ответ запрос Find pet by ID приходит с кодом 200
def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/501")
    assert response.status_code == 200

# Проверка, что в ответе приходит строчка с нужным именем
def test_piece_of_body():
    response = requests.get("https://petstore.swagger.io/v2/pet/501")
    assert response.json()['name'] == 'kokosha'
