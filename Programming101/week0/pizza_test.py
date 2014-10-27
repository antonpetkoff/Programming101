from pizza import Pizza
from os import remove
import unittest


class PizzaTests(unittest.TestCase):

    def setUp(self):
        self.pizza = Pizza()

    def test_take_order(self):
        self.pizza.take("take rado 5.0")
        self.assertEqual(self.pizza.order, {"rado": 5.0})
        self.pizza.take("take toni 6")
        self.assertEqual(self.pizza.order, {"rado": 5.0, "toni": 6.0})

    def test_save_order(self):
        self.pizza.take("take rado 5")
        self.pizza.save()
        self.assertEqual(self.pizza.loadOrder(self.pizza.orderNames[-1]),
                         {"rado": 5.0})
        remove(self.pizza.orderNames[-1])

    def test_load_order(self):
        self.pizza.take("take rado 5")
        self.pizza.save()
        self.pizza.take("take toni 60")
        self.pizza.isListCalled = True      # in order to bypass user input
        self.pizza.isLastOrderSaved = True  # in order to bypass user input
        self.pizza.load("load 1")
        self.assertEqual(self.pizza.order, {"rado": 5.0})
        remove(self.pizza.orderNames[-1])


if __name__ == '__main__':
    unittest.main()
