"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(0) is True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(11)
        assert product.quantity == 989
        product.buy(989)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1010)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 1)
        assert cart.products[product] == 2

    def test_remove_product(self, cart, product):
        cart.add_product(product, 100)
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product, 70)
        assert cart.products[product] == 30

        cart.add_product(product, 70)
        cart.remove_product(product, 100)
        assert product not in cart.products

    def test_clear(self, cart, product):
        cart.add_product(product, 100)
        assert cart.products[product] == 100
        with pytest.raises(NotImplementedError):
            cart.clear()

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 5)
        cart.get_total_price()
        assert cart.get_total_price() == 500

    def test_buy(self, cart, product):
        cart.add_product(product, 50)
        cart.buy()
        assert product.quantity == 950

        with pytest.raises(ValueError):
            cart.add_product(product, 1001)
            cart.buy()
