import unittest
from main import Product, Smartphone, LawnGrass, Category


class TestProduct(unittest.TestCase):

    def test_product_creation(self):
        p = Product("Товар", "Описание товара", 100, 10)
        self.assertEqual(p.name, "Товар")
        self.assertEqual(p.price, 100)
        self.assertEqual(p.quantity, 10)

    def test_price_setter(self):
        p = Product("Товар", "Описание товара", 100, 10)
        p.price = 120
        self.assertEqual(p.price, 120)

        with self.assertRaises(ValueError):
            p.price = -10

    def test_quantity_setter(self):
        p = Product("Товар", "Описание товара", 100, 10)
        p.quantity = 5
        self.assertEqual(p.quantity, 5)

        with self.assertRaises(ValueError):
            p.quantity = -5

    def test_product_addition(self):
        p1 = Product("Товар 1", "Описание 1", 100, 10)
        p2 = Product("Товар 2", "Описание 2", 200, 5)
        self.assertEqual(p1 + p2, 2000)  # (100*10 + 200*5), теперь 2000


class TestSmartphone(unittest.TestCase):

    def test_smartphone_creation(self):
        s = Smartphone("Телефон", "Модный смартфон", 1000, 10, "5G", "Model X", 128, "Черный")
        self.assertEqual(s.model, "Model X")
        self.assertEqual(s.memory, 128)
        self.assertEqual(s.color, "Черный")

    def test_smartphone_str(self):
        s = Smartphone("Телефон", "Модный смартфон", 1000, 10, "5G", "Model X", 128, "Черный")
        self.assertEqual(str(s), "Телефон (Model X), 128GB, Черный, 1000 руб. Остаток: 10 шт.")


class TestCategory(unittest.TestCase):

    def test_category_creation(self):
        p1 = Product("Товар 1", "Описание 1", 100, 10)
        p2 = Product("Товар 2", "Описание 2", 200, 5)
        category = Category("Категория 1", "Описание категории", [p1, p2])
        self.assertEqual(category.name, "Категория 1")
        self.assertEqual(category.product_count, 2)

    def test_add_product(self):
        p1 = Product("Товар 1", "Описание 1", 100, 10)
        category = Category("Категория 1", "Описание категории", [p1])
        p2 = Product("Товар 2", "Описание 2", 200, 5)
        category.add_product(p2)
        self.assertEqual(category.product_count, 2)

    def test_add_invalid_product(self):
        category = Category("Категория 1", "Описание категории", [])
        with self.assertRaises(TypeError):
            category.add_product("Invalid Product")

    def test_average_price(self):
        p1 = Product("Товар 1", "Описание 1", 100, 10)
        p2 = Product("Товар 2", "Описание 2", 200, 5)
        category = Category("Категория 1", "Описание категории", [p1, p2])
        self.assertEqual(category.average_price(), 150)  # (100 + 200) / 2 = 150

    def test_average_price_with_no_products(self):
        category = Category("Категория 2", "Описание категории", [])
        self.assertEqual(category.average_price(), 0)  # Нет продуктов, должно вернуть 0


if __name__ == "__main__":
    unittest.main()
