import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from delivery_service import calculate_delivery_cost
class TestDeliveryService(unittest.TestCase):
    def test_basic_delivery_cost(self):
        cost, date = calculate_delivery_cost(10, 1000, "обычный")
        self.assertEqual(cost, 6240)

    def test_express_delivery_bug(self):
        """Этот тест УПАДЕТ, так как найдет баг с дешевым экспрессом"""
        cost_normal, _ = calculate_delivery_cost(10, 1000, "обычный")
        cost_express, _ = calculate_delivery_cost(10, 1000, "обычный", is_express=True)
        self.assertGreater(cost_express, cost_normal, "Express доставка должна стоить дороже обычной!")

    def test_fragile_package_surcharge(self):
        cost, _ = calculate_delivery_cost(1, 100, "хрупкий")
        self.assertEqual(cost, 1000)

    def test_dangerous_package_surcharge(self):
        cost, _ = calculate_delivery_cost(1, 100, "опасный")
        self.assertEqual(cost, 1700)

    def test_heavy_weight_coefficient(self):
        cost, _ = calculate_delivery_cost(25, 100, "обычный")
        self.assertEqual(cost, 1050)

    def test_boundary_weight_excluded(self):
        cost, _ = calculate_delivery_cost(5.0, 100, "обычный")
        self.assertEqual(cost, 700)

    def test_invalid_weight_too_light(self):
        cost, date = calculate_delivery_cost(0.05, 100, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_distance_too_far(self):
        cost, date = calculate_delivery_cost(10, 5001, "обычный")
        self.assertEqual(cost, -1)

    def test_invalid_package_type(self):
        cost, date = calculate_delivery_cost(10, 100, "золотой")
        self.assertEqual(cost, -1)

    def test_delivery_date_calculation(self):
        _, date = calculate_delivery_cost(10, 1000, "обычный")
        self.assertEqual(date, "2026-09-05")

if __name__ == '__main__':
    unittest.main()