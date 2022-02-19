import unittest

from domain.board import Board, Radar
from domain.ship import Ship
from player.computer import Computer
from player.human import Human
from repository.ocean import Ocean
from strategy.dumbStrat import BasicBot


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 5)
        self.radar = Radar(5, 5)

        self.ocean_human = Ocean(self.board)
        self.ocean_pc = Ocean(self.radar)

        # self.player_human = Human(self.board, self.radar)

        self.strat = BasicBot()
        self.player_pc = Computer(self.board, self.radar, self.strat)

        self.s1 = Ship(2, "b", 3, "b", 1)
        self.ocean_human.place_ship(self.s1)

    def test_blind_shot(self):

        self.strat.call_blind_shot(self.board, 1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . ~ ~ ~ ~\n"
                         " 2 ~ 1 ~ ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.strat.call_blind_shot(self.board, 2, 2)
        self.assertEqual("   a b c d e\n"
                         " 1 . ~ ~ ~ ~\n"
                         " 2 ~ X ~ ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))
        self.assertEqual(1, self.strat.len_stack())

    def test_strike(self):
        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . ~ ~ ~ ~\n"
                         " 2 ~ 1 ~ ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))
        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . ~ . ~ ~\n"
                         " 2 ~ 1 ~ ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))
        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . ~ . ~ .\n"
                         " 2 ~ 1 ~ ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))
        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . ~ . ~ .\n"
                         " 2 ~ X ~ ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 ~ X ~ ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))
        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 ~ X . ~ ~\n"
                         " 3 ~ 1 ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 ~ X . ~ ~\n"
                         " 3 ~ X ~ ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 ~ X . ~ ~\n"
                         " 3 ~ X . ~ ~\n"
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 ~ X . ~ ~\n"
                         " 3 ~ X . ~ ~\n"
                         " 4 ~ . ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 ~ X . ~ ~\n"
                         " 3 . X . ~ ~\n"
                         " 4 ~ . ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 . X . ~ ~\n"
                         " 3 . X . ~ ~\n"
                         " 4 ~ . ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))

        self.player_pc.strike(1, 1)
        self.assertEqual("   a b c d e\n"
                         " 1 . . . ~ .\n"
                         " 2 . X . . ~\n"
                         " 3 . X . ~ ~\n"
                         " 4 ~ . ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n", str(self.board))



    def test_status_cell(self):
        self.assertEqual(True, self.strat.call_status_cell(self.board, 0, 1))
        self.assertEqual(False, self.strat.call_status_cell(self.board, 6, 6))
        self.player_pc.strike(1, 1)
        self.assertEqual(False, self.strat.call_status_cell(self.board, 0, 0))





