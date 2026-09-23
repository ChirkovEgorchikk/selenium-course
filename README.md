# Selenium + Python: автотесты для интернет-магазина

Учебный проект по курсу «Автоматизация тестирования с помощью Selenium и Python» (Stepik).

В проекте реализованы автотесты для демонстрационного интернет-магазина
[http://selenium1py.pythonanywhere.com/](http://selenium1py.pythonanywhere.com/).

## 📁 Структура проекта
├── pages/
│ ├── init.py # делает папку пакетом Python
│ ├── base_page.py # базовый класс BasePage с общими методами
│ ├── locators.py # все локаторы вынесены отдельно
│ └── product_page.py # Page Object для страницы товара
├── conftest.py # фикстура browser с параметром --language
├── test_items.py # тест наличия кнопки "Добавить в корзину"
├── test_product_page.py # тесты страницы товара (в т.ч. параметризованные)
└── README.md


## ⚙️ Требования

- Python 3.10+
- Google Chrome (актуальная версия)
- ChromeDriver (подходящей версии — можно положить в `PATH` или рядом с проектом)
- Установленные библиотеки:

```bash
pip install selenium pytest

Что реализовано
Page Object для главной страницы и страницы товара.

BasePage с методами open(), is_element_present(), solve_quiz_and_get_code().

Локаторы вынесены в отдельный файл locators.py — при изменении вёрстки
правится только одно место.

Проверки, независимые от данных: название и цена товара берутся со
страницы, а не захардкожены.

Параметризация через @pytest.mark.parametrize для промо-акций
offer0–offer9.

Метка xfail для известного бага на ?promo=offer7 (в сообщении
появляется лишнее слово «book»).

Фикстура browser с поддержкой параметра --language для запуска
тестов на разных языках интерфейса.

 Найденный баг
При открытии страницы
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7
в сообщении об успешном добавлении товара в корзину выводится название
«Coders at Work book», тогда как сам товар называется «Coders at Work».
Тест ловит это расхождение и помечен как xfail, так как баг пока не исправлен.
