from abc import ABC, abstractmethod


# Абстрактный класс BaseProduct
class BaseProduct(ABC):
    @abstractmethod
    def product_info(self):
        pass


# Миксин для вывода информации
class PrinterMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        return f"Создан объект класса {self.__class__.__name__} с параметрами {self.__dict__}"


# Класс Product, который наследует BaseProduct и PrinterMixin
class Product(PrinterMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.__quantity = quantity  # Приватный атрибут
        super().__init__()  # Вызов конструктора PrinterMixin

    @property
    def price(self):
        return self.__price  # Теперь доступ к приватному атрибуту

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value  # Приватный атрибут
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

    @property
    def quantity(self):
        return self.__quantity  # Приватный атрибут

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self.__quantity = value  # Приватный атрибут
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

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)


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
        self.__products = products  # Приватный атрибут для списка продуктов

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект класса Product или его наследников")
        self.__products.append(product)

    @property
    def product_count(self):
        return len(self.__products)

    @property
    def products(self):
        return "\n".join([str(product) for product in self.__products]) + "\n"

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    # Добавление метода для вычисления средней цены
    def average_price(self):
        try:
            if len(self.__products) == 0:
                return 0
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0  # Возвращаем 0, если сумма всех товаров делится на ноль
