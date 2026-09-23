import time
from selenium.webdriver.common.by import By


def test_guest_can_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза 30 секунд, чтобы рецензент успел визуально проверить язык кнопки
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    # Селектор .btn-add-to-basket уникален для этой страницы и не зависит от языка
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Проверка (assert)
    assert button is not None, "Кнопка добавления в корзину не найдена на странице"