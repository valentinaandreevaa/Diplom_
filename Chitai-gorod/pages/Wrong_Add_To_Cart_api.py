import requests
import json
import allure
from constants import API1_url
from constants import API2_url
from constants import bearer_token

@allure.description("Тестирование добавления товара в корзину на сайте Читай-город.")
class WrongRequestAPI:

    url = API1_url
    url_2 = API2_url

    def __init__(self, url: str):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': bearer_token
        }

    def wrong_add_product(self, product_id: int, item_list_name: str) -> requests.Response:
        payload = {
            "id": product_id,
            "adData": {
                "item_list_name": item_list_name,
            }
        }
        resp = requests.patch(self.url, headers=self.headers, data=json.dumps(payload))
        return resp.status_code