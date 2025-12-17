# test_shipping.py

import unittest
from shipping import shipping_cost


class TestShippingCost(unittest.TestCase):

    def test_one_item(self):
        self.assertEqual(shipping_cost(1), 10.95)

    def test_two_items(self):
        self.assertEqual(shipping_cost(2), 13.90)

    def test_multiple_items(self):
        self.assertEqual(shipping_cost(5), 10.95 + 4 * 2.95)

    def test_zero_items(self):
        self.assertEqual(shipping_cost(0), 0)

    def test_negative_items(self):
        self.assertEqual(shipping_cost(-3), 0)


if __name__ == '__main__':
    unittest.main()
