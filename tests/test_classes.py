import pytest
from main import Product, Category


@pytest.fixture(autouse=True)
def reset_category_and_product_count():
    """Фикстура для сброса счетчиков перед каждым тестом."""
    Category.reset()


def test_count_products_and_categories():
    # Создаем продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создаем первую категорию с продуктами
    category = Category("Смартфоны", "Описание категории смартфонов", [product1, product2])

    # Проверка на количество категорий и товаров
    assert Category.category_count == 1  # Ожидается 1 категория
    assert Category.product_count == 2  # Ожидается 2 продукта в системе


def test_category_and_product_count():
    # Создаем продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создаем первую категорию с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        [product1, product2],
    )

    # Создаем вторую категорию и продукты
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться "
                           "просмотром", [product3])

    # Проверка общего количества категорий и продуктов
    assert Category.category_count == 2  # Ожидается 2 категории
    assert Category.product_count == 3  # Ожидается 3 продукта в системе


def test_getter_products():
    product1 = Product("Samsung Galaxy S23", "256GB, Серый цвет", 150000, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создаем категорию с продуктами
    category = Category("Смартфоны", "Мобильные телефоны", [product1, product2])

    # Проверяем работу геттера
    expected_products = (
        "Samsung Galaxy S23, 150000 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category.products == expected_products
