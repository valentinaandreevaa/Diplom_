import requests
import json
import allure
from constants import API1_url, API2_url, bearer_token


@allure.title("Класс для удаления товара из корзины")
class DeleteFromCart:
    url = API1_url  
    url_2 = API2_url  

    @allure.step("Инициализация класса DeleteFromCart")
    def __init__(self, url):
        """
        Создаем объект для работы с корзиной.

        :param url: URL для удаления товара из корзины.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',  
            'Authorization': bearer_token  
        }

    @allure.step("Получение содержимого корзины")
    def get_cart_contents(self)-> dict:
        """
        Получает содержимое корзины.

        :return: Статус-код ответа и содержимое корзины в формате JSON.
        """
        response = requests.get(self.url_2, headers=self.headers)
        return response.status_code, response.json()  

    @allure.step("Удаление товара из корзины")
    def delete_product_from_cart(self, prod_id)-> None:
        """
        Удаляем товар из корзины.

        :param prod_id: ID товара, который нужно удалить.
        :return: Статус-код ответа от сервера.
        """
        response = requests.delete(self.url_2, headers=self.headers, data=json.dumps(prod_id))
        return response.status_code  