class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут для цены
        self._quantity = quantity  # Приватный атрибут для количества

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой на положительное значение."""
        if value > 0:
            self._price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @property
    def quantity(self):
        """Геттер для количества."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Сеттер для количества."""
        if value >= 0:
            self._quantity = value
        else:
            print("Количество не может быть отрицательным")


class Category:
    category_count = 0  # Количество категорий
    product_count = 0  # Количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products = products  # Приватный атрибут для списка продуктов

        # Увеличиваем количество категорий
        Category.category_count += 1

        # Увеличиваем количество продуктов, добавленных в эту категорию
        Category.product_count += len(products)

    @classmethod
    def reset(cls):
        """Метод для сброса счетчиков категорий и продуктов."""
        cls.category_count = 0
        cls.product_count = 0

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка продуктов."""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
             for product in self._products]
        ) + "\n"  # Добавляем '\n' в конце
