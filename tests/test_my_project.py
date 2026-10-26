import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from my_project import calculate_triangle

class TestTriangleCalculator(unittest.TestCase):
    def test_valid_equilateral_triangle(self):
        t_type, coords = calculate_triangle("5", "5", "5")
        self.assertEqual(t_type, "равносторонний")

    def test_valid_isosceles_triangle(self):
        t_type, coords = calculate_triangle("5", "5", "8")
        self.assertEqual(t_type, "равнобедренный")

    def test_valid_scalene_triangle(self):
        t_type, coords = calculate_triangle("3", "4", "6")
        self.assertEqual(t_type, "разносторонний")

    def test_valid_right_triangle(self):
        t_type, coords = calculate_triangle("3", "4", "5")
        self.assertEqual(t_type, "прямоугольный")

    def test_invalid_negative_side(self):
        t_type, coords = calculate_triangle("-1", "5", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_invalid_zero_side(self):
        t_type, coords = calculate_triangle("0", "5", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_invalid_triangle_inequality(self):
        t_type, coords = calculate_triangle("1", "1", "3")
        self.assertEqual(t_type, "не треугольник")

    def test_invalid_string_input(self):
        t_type, coords = calculate_triangle("abc", "5", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_float_sides(self):
        t_type, coords = calculate_triangle("3.5", "4.5", "5.5")
        self.assertNotEqual(t_type, "не треугольник")

    def test_degenerate_triangle(self):
        t_type, coords = calculate_triangle("1", "2", "3")
        self.assertEqual(t_type, "не треугольник")

if __name__ == '__main__':
    unittest.main()