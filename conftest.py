import pytest
from helpers import create_random_login, create_random_password, create_random_firstname  
import requests  
from urls import Urls

@pytest.fixture
def generate_create_data_and_delete_courier():
    #Генерируем тестовые данные для создания курьера.
    payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
    
    yield payload
    #Удаляем курьера после выполнения тесста.
    data = {'login': payload['login'],
            'password': payload['password']}
    #Получаем id курьера. Его возвращает ручка login.
    respons = requests.post(Urls.URL_courier_login, data)
    #Удаляем курьера, используя id, который получили от login.
    requests.post(f'{Urls.URL_courier_delete}{respons[id]}')
    