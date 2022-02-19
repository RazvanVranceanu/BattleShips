import unittest

from domain.ship import Ship
from exception.exceptions import ValidationException
from game.game import Game
from validators.validators import Validators, is_char


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.validators = Validators()

    def test_is_char(self):
        self.assertEqual(True, is_char("a"))
        self.assertEqual(False, is_char("abc"))

    def test_validate_orientation(self):
        with self.assertRaises(ValidationException) as ve:
            self.validators.validate_orientation("hh")
        self.assertEqual(str(ve.exception), "Invalid orientation!\n")

        with self.assertRaises(ValidationException) as ve:
            self.validators.validate_orientation("z")
        self.assertEqual(str(ve.exception), "Invalid orientation!\n")

    def test_validate_ship(self):
        s1 = Ship(11, "a", 2, "g", 0)
        s2 = Ship(0, "a", 2, "hh", 0)
        s3 = Ship(1, "a", 2, "k", 0)

        with self.assertRaises(ValidationException) as ve:
            self.validators.validate(s1)
        self.assertEqual(str(ve.exception), "Invalid line!\n")
        with self.assertRaises(ValidationException) as ve:
            self.validators.validate(s2)
        self.assertEqual(str(ve.exception), "Invalid line!\nInvalid column!\n")
        with self.assertRaises(ValidationException) as ve:
            self.validators.validate(s3)
        self.assertEqual(str(ve.exception), "Invalid column!\n")

    def test_validate_with_orientation(self):
        def get_second_coordinates(line, column, orientation, dimension):
            if orientation == "v":
                return line + dimension - 1, column
            return line, chr(ord(column) + dimension - 1)
        x1 = 10
        y1 = "j"
        x2, y2 = get_second_coordinates(x1, y1, "v", 3)
        s1 = Ship(x1, y1, x2, y2, 0)
        with self.assertRaises(ValidationException) as ve:
            self.validators.validate(s1)
        self.assertEqual(str(ve.exception), "Invalid line!\n")

        x2, y2 = get_second_coordinates(x1, y1, "h", 3)
        s2 = Ship(x1, y1, x2, y2, 0)
        with self.assertRaises(ValidationException) as ve:
            self.validators.validate(s2)
        self.assertEqual(str(ve.exception), "Invalid column!\n")

    def test_validate_strike(self):
        with self.assertRaises(ValidationException) as ve:
            self.validators.validate_strike(1, "k")
        self.assertEqual(str(ve.exception), "Invalid column!\n")

        with self.assertRaises(ValidationException) as ve:
            self.validators.validate_strike(12, "f")
        self.assertEqual(str(ve.exception), "Invalid line!\n")


if __name__ == '__main__':
    unittest.main()
