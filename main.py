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
        print(f"Создан объект класса {self.__class__.__name__} с параметрами {args}, {kwargs}")
        super().__init__(*args, **kwargs)


# Класс Product, который наследует BaseProduct и PrinterMixin
class Product(PrinterMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
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


# Пример работы программы
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.product_count)
    print(Category.product_count)
