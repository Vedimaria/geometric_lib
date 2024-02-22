import unittest
import circle
import rectangle


class CircleTestCase(unittest.TestCase):
    def test_big_data(self):
        self.assertEqual(circle.area(10_000_000), 314_159_265_358_979.3)
        self.assertEqual(circle.perimeter(10_000_000), 62_831_853.071795866)

    def test_negative(self):
        self.assertEqual(circle.area(-10), "Error: Negative Length")
        self.assertEqual(circle.perimeter(-10), "Error: Negative Length")

    def test_zero(self):
        self.assertEqual(circle.area(0), "Error: Zero Length")
        self.assertEqual(circle.perimeter(0), "Error: Zero Length")

    def test_string(self):
        self.assertEqual(circle.area("abcd"), "Error: Invalid Length")
        self.assertEqual(circle.perimeter("abcd"), "Error: Invalid Length")

    def test_float(self):
        self.assertEqual(circle.area(0.5), "Error: Not Integer Length")
        self.assertEqual(circle.perimeter(0.5), "Error: Not Integer Length")


class RectangleTestCase(unittest.TestCase):
    def test_big_data(self):
        self.assertEqual(rectangle.area(10_000_000, 1_000_000), 10_000_000_000_000)
        self.assertEqual(rectangle.perimeter(10_000_000, 1_000_000), 22_000_000)

    def test_negative(self):
        self.assertEqual(rectangle.area(-10, 5), "Error: Negative Length")
        self.assertEqual(rectangle.perimeter(-10, 5), "Error: Negative Length")

    def test_zero(self):
        self.assertEqual(rectangle.area(10, 0), "Error: Zero Length")
        self.assertEqual(rectangle.perimeter(10, 0), "Error: Zero Length")

    def test_string(self):
        self.assertEqual(rectangle.area(10, "abcd"), "Error: Invalid Length")
        self.assertEqual(rectangle.perimeter(10, "abcd"), "Error: Invalid Length")

    def test_float(self):
        self.assertEqual(rectangle.area(10, 0.5), "Error: Not Integer Length")
        self.assertEqual(rectangle.perimeter(10, 0.5), "Error: Not Integer Length")

