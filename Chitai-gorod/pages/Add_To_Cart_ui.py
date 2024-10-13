from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@allure.description("Добавление товара в корзину на сайте Читай-город.")
class AddToCart:
  
    # ИНИЦИАЛИЗАЦИЯ
    def __init__(self, book_title: str):
        """         Создаем объект для добавления книги в корзину.

                    :param book_title: Название книги для добавления в корзину.
        """
        self.book_title = book_title

    # ПОИСК КНИГИ ПО НАЗВАНИЮ
    def search_by_title(self, driver: webdriver.Chrome, book_title: str) -> dict:
        """         Ищем книгу по названию и добавляем её в корзину.

                    :param driver: Экземпляр драйвера Selenium.
                    :param book_title: Название книги для поиска.
                    :return: Словарь с результатами поиска (в данном методе возвращает None).
        """
        # Ввод названия книги в строку поиска
        driver.find_element(By.NAME, "phrase").send_keys(book_title)
        
        # Клик по кнопке поиска
        search_button_find = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Искать']")
        search_button_find.click()

        # Клик по кнопке "Купить"
        search_button_buy = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Купить']")
        search_button_buy.click() 
        
        # Открытие корзины
        cart_icon = driver.find_element(By.CSS_SELECTOR, '.header-cart__icon')
        cart_icon.click()