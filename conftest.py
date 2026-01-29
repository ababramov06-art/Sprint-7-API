import pytest
from helpers import create_random_login, create_random_password, create_random_firstname  
import requests  
from urls import Urls

@pytest.fixture
def generate_create_data():
    payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
    
    yield payload
    data = {'login': payload['login'],
            'password': payload['password']}
    respons = requests.post(Urls.URL_courier_login, data)
    requests.post(f'{Urls.URL_courier_create}:{respons[id]}')