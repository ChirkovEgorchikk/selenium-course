from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        """Возвращает название товара со страницы."""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает цену товара со страницы."""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_added_to_basket(self):
        """Название товара в сообщении совпадает с названием на странице."""
        self.solve_quiz_and_get_code()
        product_name = self.get_product_name()
        message_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        assert product_name == message_name, (
            f"Название в сообщении '{message_name}' "
            f"не совпадает с названием товара '{product_name}'"
        )

    def should_be_correct_basket_total(self):
        """Стоимость корзины совпадает с ценой товара."""
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_PRICE
        ).text
        assert product_price == basket_total, (
            f"Стоимость корзины '{basket_total}' "
            f"не совпадает с ценой товара '{product_price}'"
        )