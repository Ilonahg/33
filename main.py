class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0  # Количество категорий
    product_count = 0  # Количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем количество категорий
        Category.category_count += 1

        # Увеличиваем количество продуктов, добавленных в эту категорию
        Category.product_count += len(products)

    @classmethod
    def reset(cls):
        """Метод для сброса счетчиков категорий и продуктов."""
        cls.category_count = 0
        cls.product_count = 0