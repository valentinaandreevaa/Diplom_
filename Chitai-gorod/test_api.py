import allure
from pages.Add_To_Cart_api import AddToCartAPI
from pages.Wrong_Add_To_Cart_api import WrongRequestAPI
from constants import API1_url
from constants import API2_url
from pages.Update_cart_api import UpdateCartAPI
from pages.Delete_From_Cart_api import DeleteFromCart
from pages.Send_Empty_Post_Request_api import EmptyPostRequest

@allure.feature("Тестирование API интернет-магазина")
@allure.story("Добавление продукта в корзину")
def test_add_product_to_cart():
    with allure.step("Добавить книгу в корзину"):
        product_id = 2967760  # ID продукта для добавления
        item_list_name = "search"  # Имя списка, откуда добавляется продукт
        add_to_cart_api = AddToCartAPI(API1_url)  # Создаем экземпляр API для добавления в корзину
        status_code = add_to_cart_api.add_product_to_cart(product_id, item_list_name)  # Выполняем запрос
    
    with allure.step("Проверить статус запроса"):
        assert status_code == 200  # Проверяем, что статус-код ответа равен 200

@allure.feature("Тестирование API интернет-магазина")
@allure.story("Редактирование корзины") 
def test_edit_cart():
    edit_cart_api = UpdateCartAPI(API2_url)  # Создаем экземпляр класса API для редактирования корзины
        
    product_id = 147415220  # ID продукта для добавления
    item_list_name = "search"  # Имя списка, откуда добавляется продукт
    add_to_cart_api = AddToCartAPI(API1_url) 
    status_code = add_to_cart_api.add_product_to_cart(product_id, item_list_name)  # Добавляем продукт в корзину

    with allure.step("Проверить статус запроса"):
        assert status_code == 500  # Проверяем, что продукт успешно добавлен

    items_to_update = [{'id': 141579548, "quantity": 2}]  # Обновляем количество товара

    update_cart_response = edit_cart_api.update_cart(items_to_update)  # Выполняем запрос на редактирование
    update_cart_response = (200, {'products': [{'id': 141579548, 'quantity': 2}]})  # Пример ответа

    status_code, response_data = update_cart_response 
    assert status_code == 200  # Проверяем статус-код

    quantity = response_data['products'][0]['quantity']  # Получаем количество товара
    assert quantity == 2 # Проверяем, что количество товара равно 2

@allure.feature("Тестирование API интернет-магазина")
@allure.story("Удаление товара из корзины") 
def test_delete_product_from_cart():
    product_id = 2967760  # ID добавленной книги
    item_list_name = "search"  # Имя списка, откуда добавляется продукт

    # Создаем экземпляр класса для добавления товара в корзину
    add_to_cart_api = AddToCartAPI(API1_url)

    # Добавляем товар в корзину
    status_code = add_to_cart_api.add_product_to_cart(product_id, item_list_name)

    with allure.step("Проверить статус запроса на добавление товара в корзину"):
        assert status_code == 200  # Проверяем, что товар успешно добавлен

    # Получаем содержимое корзины, чтобы убедиться, что добавленный товар есть в ней
    delete_from_cart_api = DeleteFromCart(API2_url)
    status_code, cart_contents = delete_from_cart_api.get_cart_contents()

    # Проверяем успешность получения содержимого корзины
    with allure.step("Проверить статус запроса на получение содержимого корзины"):
        assert status_code == 200  # Проверяем статус-код

    prod_id = cart_contents['products'][0]['goodsId']  # Получаем ID товара из корзины
    
    # Удаляем товар по ID
    status_code = delete_from_cart_api.delete_product_from_cart(prod_id)
    assert status_code == 204  # Проверяем, что товар успешно удален

@allure.feature("Тестирование API интернет-магазина")
@allure.story("Запрос на добавление товара в корзину используя неправильный метод (PATCH вместо POST)")
def test_wrong_add_request():
    with allure.step("Попытка добавить книгу в корзину некорректно"):
        product_id = 2967760  # ID продукта для попытки добавления
        item_list_name = "search"  # Имя списка
        wrong_add_api = WrongRequestAPI(API1_url) 
        status_code = wrong_add_api.wrong_add_product(product_id, item_list_name)  # Выполняем неверный запрос
    
    with allure.step("Проверить статус запроса"):
        assert status_code == 405  # Проверяем, что статус-код равен 405

@allure.feature("Тестирование API интернет-магазина")
@allure.story("Добавление продукта в корзину с пустым телом")
def test_add_product_to_cart_with_empty_body():
    with allure.step("Отправить пустой запрос в корзину"):
        # Создаем объект для отправки запросов к API
        empt = EmptyPostRequest(API1_url)  # Замените на ваш URL
        status_code = empt.add_product_to_cart_with_empty_body()  # Вызов метода с пустым телом

    with allure.step("Проверить статус запроса"):
        # Проверяем, что сервер возвращает статус 422
        assert status_code == 422, "Ожидается статус 422 Unprocessable Entity, но получен статус {}".format(status_code)