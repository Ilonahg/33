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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операция поддерживается только для объектов класса Product")


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
            [str(product) for product in self._products]
        ) + "\n"  # Добавляем '\n' в конце

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
