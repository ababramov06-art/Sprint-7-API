import requests
import allure
import pytest
from urls import Urls


class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и тело ответа.')
    @allure.step('Получение списка заказов.')
    def test_orders_list_get_success(self):
        response = requests.get(Urls.URL_orders_create)
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]
