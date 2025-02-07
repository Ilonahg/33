from abc import ABC, abstractmethod


# Абстрактный класс BaseProduct
class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self._quantity = quantity

    @abstractmethod
    def product_info(self):
        pass


# Миксин для вывода информации
class PrinterMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами {args}, {kwargs}")


# Класс Product, который наследует BaseProduct и PrinterMixin
class Product(PrinterMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self._quantity = value
        else:
            raise ValueError("Количество не может быть отрицательным")

    def product_info(self):
        return f"Product: {self.name}, {self.description}, {self.price}, {self.quantity}"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операция поддерживается только для объектов класса Product")


# Класс Smartphone, наследующий от Product
class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name} ({self.model}), {self.memory}GB, {self.color}, {self.price} руб. Остаток: {self.quantity} шт."


# Класс LawnGrass, наследующий от Product
class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def product_info(self):
        return f"Grass: {self.name}, {self.description}, {self.price}, {self.quantity}, Country: {self.country}, Germination Period: {self.germination_period}, Color: {self.color}"


# Класс Category для организации продуктов по категориям
class Category:
    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products = products

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект класса Product или его наследников")
        self._products.append(product)

    @property
    def product_count(self):
        return len(self._products)

    @property
    def products(self):
        return "\n".join([str(product) for product in self._products]) + "\n"

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    # Добавление метода для вычисления средней цены
    def average_price(self):
        if len(self._products) == 0:
            return 0
        total_price = sum(product.price for product in self._products)
        return total_price / len(self._products)
