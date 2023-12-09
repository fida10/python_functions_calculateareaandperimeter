import unittest
from src.ans import calculate_area_perimeter


class TestCalculateAreaPerimeter(unittest.TestCase):

    def test_area_perimeter(self):
        area, perimeter = calculate_area_perimeter(5, 3)
        self.assertEqual(area, 15)
        self.assertEqual(perimeter, 16)

    def test_zero_values(self):
        area, perimeter = calculate_area_perimeter(0, 5)
        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 10)


if __name__ == '__main__':
    unittest.main()
