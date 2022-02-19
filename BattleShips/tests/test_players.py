import unittest

from domain.board import Board, Radar
from domain.ship import Ship
from exception.exceptions import StrikeError
from player.computer import Computer
from player.human import Human
from repository.ocean import Ocean
from strategy.noStrat import NoStrategy


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 5)
        self.radar = Radar(5, 5)
        self.ocean_human = Ocean(self.board)
        self.ocean_pc = Ocean(self.radar)
        self.player_human = Human(self.board, self.radar)
        strat = NoStrategy()
        self.player_pc = Computer(self.board, self.radar, strat)

        self.s1 = Ship(1, "a", 2, "a", 1)
        self.ocean_pc.place_ship(self.s1)
        self.ocean_human.place_ship(self.s1)

    def test_strike_human(self):
        self.assertEqual(str(self.ocean_pc.get_board()), "   a b c d e\n"
                                                         " 1 ~ ~ ~ ~ ~\n"
                                                         " 2 ~ ~ ~ ~ ~\n"
                                                         " 3 ~ ~ ~ ~ ~\n"
                                                         " 4 ~ ~ ~ ~ ~\n"
                                                         " 5 ~ ~ ~ ~ ~\n")
        self.player_human.strike(1, "a")
        self.assertEqual(str(self.ocean_pc.get_board()), "   a b c d e\n"
                                                         " 1 X ~ ~ ~ ~\n"
                                                         " 2 ~ ~ ~ ~ ~\n"
                                                         " 3 ~ ~ ~ ~ ~\n"
                                                         " 4 ~ ~ ~ ~ ~\n"
                                                         " 5 ~ ~ ~ ~ ~\n")
        self.player_human.strike(4, "c")
        self.assertEqual(str(self.ocean_pc.get_board()), "   a b c d e\n"
                                                         " 1 X ~ ~ ~ ~\n"
                                                         " 2 ~ ~ ~ ~ ~\n"
                                                         " 3 ~ ~ ~ ~ ~\n"
                                                         " 4 ~ ~ . ~ ~\n"
                                                         " 5 ~ ~ ~ ~ ~\n")
        with self.assertRaises(StrikeError) as se:
            self.player_human.strike(1, "a")

        self.assertEqual(str(se.exception), "Can't fire twice in the same spot! Try again!")

    def test_strike_pc(self):
        self.player_pc.strike(1, "a")
        print(self.board)
        self.player_pc.strike(2, "a")
        print(self.board)
