import unittest

from domain.board import Board, Radar


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 5)

    def test_create(self):
        self.assertEqual(str(self.board), "   a b c d e\n"
                                          " 1 ~ ~ ~ ~ ~\n"
                                          " 2 ~ ~ ~ ~ ~\n"
                                          " 3 ~ ~ ~ ~ ~\n"
                                          " 4 ~ ~ ~ ~ ~\n"
                                          " 5 ~ ~ ~ ~ ~\n")

    def test_set_n_get_cell(self):
        self.board.set_value(1, "a", 1)
        self.assertEqual(self.board.get_value(1, "a"), 1)


    def test_radar(self):
        radar = Radar(3, 3)
        radar.set_value(1, "a", 1)
        radar.set_value(2, "b", "X")
        radar.set_value(3, "c", ".")
        self.assertEqual(str(radar), "   a b c\n"
                                     " 1 ~ ~ ~\n"
                                     " 2 ~ X ~\n"
                                     " 3 ~ ~ .\n")
