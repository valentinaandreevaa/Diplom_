import requests
import allure
from constants import API1_url
from constants import bearer_token

@allure.description("Тестирование отправки пустого запроса к API .")
class EmptyPostRequest:
    url = API1_url
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',  # Указываем, что отправляем JSON
            'Authorization': bearer_token  # Токен для авторизации
        }

    def add_product_to_cart_with_empty_body(self)-> None:
        response = requests.post(self.url, json={}, headers=self.headers)  # Отправляем пустое тело
        return response.status_code