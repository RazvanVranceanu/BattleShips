import unittest

from domain.board import Board, Radar
from domain.ship import Ship
from exception.exceptions import ShipPlacementError
from repository.ocean import Ocean, check_order


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(10, 10)
        self.ocean = Ocean(self.board)
        self.s1 = Ship(2, "a", 5, "a", 9)
        self.s2 = Ship(4, "d", 4, "f", 4)

    def test_place(self):
        self.ocean.place_ship(self.s1)
        self.ocean.place_ship(self.s2)
        self.assertEqual(str(self.board), "   a b c d e f g h i j\n"
                                          " 1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 2 9 ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 3 9 ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 4 9 ~ ~ 4 4 4 ~ ~ ~ ~\n"
                                          " 5 9 ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 6 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 7 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 8 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 9 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          "10 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")

    def test_placement_error(self):
        self.ocean.place_ship(self.s1)
        s3 = Ship(4, "a", 7, "a", 1)
        with self.assertRaises(ShipPlacementError) as spe:
            self.ocean.place_ship(s3)

        self.assertEqual(str(spe.exception), "Can't place the ship there!")

    def test_placement_reversed(self):
        self.s3 = Ship(9, "a", 5, "a", 2)
        self.s4 = Ship(4, "f", 4, "d", 4)
        self.ocean.place_ship(self.s1)
        self.ocean.place_ship(self.s2)
        self.assertEqual(str(self.board), "   a b c d e f g h i j\n"
                                          " 1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 2 9 ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 3 9 ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 4 9 ~ ~ 4 4 4 ~ ~ ~ ~\n"
                                          " 5 9 ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 6 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 7 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 8 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          " 9 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
                                          "10 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")

    def test_reverse(self):
        a = 15
        b = 10
        a, b = check_order(a, b)
        self.assertEqual(a, 10)
        self.assertEqual(b, 15)


    def test_get_ship_status_2(self):
        radar = Radar(10, 10)
        ocean2 = Ocean(radar)
        ocean2.place_ship(self.s1)
        self.assertEqual(ocean2.get_ship_status(self.s1), True)
        radar.set_value(2, "a", "X")
        radar.set_value(3, "a", "X")
        radar.set_value(4, "a", "X")
        self.assertEqual(ocean2.get_ship_status(self.s1), True)
        radar.set_value(5, "a", "X")
        self.assertEqual(ocean2.get_ship_status(self.s1), False)



