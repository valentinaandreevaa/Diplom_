from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@allure.description("Тестирование удаления товара из корзины на сайте Читай-город.")
class DeleteFromCart:

    def __init__(self, book_title: str):
        self.book_title = book_title

    @allure.step("Поиск книги по названию и удаление из корзины")
    def delete_from_cart(self, driver: webdriver.Chrome) -> None:
    
            # Поиск книги по названию
        driver.find_element(By.NAME, "phrase").send_keys(self.book_title)

            # Клик по кнопке поиска
        search_button_find = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Искать']")
        search_button_find.click()

            # Клик по кнопке "Купить"
        search_button_buy = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Купить']")
        search_button_buy.click()

            # Открытие корзины
        cart_icon = driver.find_element(By.CSS_SELECTOR, '.header-cart__icon')
        cart_icon.click()

            # Клик по кнопке "Очистить корзину"
        delete_button = driver.find_element(By.CSS_SELECTOR, 'span.clear-cart')
        delete_button.click()