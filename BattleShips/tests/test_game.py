import unittest

from domain.board import Board, Radar
from game.game import Game
from player.computer import Computer
from player.human import Human
from repository.ocean import Ocean
from strategy.dumbStrat import BasicBot
from validators.validators import Validators


class GameTesting(unittest.TestCase):
    def setUp(self):
        board = Board(5, 5)
        radar = Radar(5, 5)
        self.ocean_human = Ocean(board)
        self.ocean_pc = Ocean(radar)
        strategy = BasicBot()
        player1 = Human(board, radar)
        player2 = Computer(board, radar, strategy)
        validators = Validators()
        self.game = Game(self.ocean_human, self.ocean_pc, player1, player2, validators)

    def test_get_second_coord(self):
        line, column = self.game.get_second_coordinates(1, "a", "h", 2)
        self.assertEqual(1, line)
        self.assertEqual("b", column)
        line, column = self.game.get_second_coordinates(1, "a", "v", 2)
        self.assertEqual(2, line)
        self.assertEqual("a", column)

    def test_place_boat_human(self):
        self.game.place_boat_human(1, "a", "h", 1, 2)
        ocean = self.game.get_ocean()
        self.assertEqual(str(ocean), "   a b c d e\n"
                                     " 1 1 1 ~ ~ ~\n"
                                     " 2 ~ ~ ~ ~ ~\n"
                                     " 3 ~ ~ ~ ~ ~\n"
                                     " 4 ~ ~ ~ ~ ~\n"
                                     " 5 ~ ~ ~ ~ ~\n")

    def test_place_boat_pc(self):
        self.game.place_boat_pc(1, "a", "h", 1, 2)
        ocean = self.game.get_radar()
        self.assertEqual(str(ocean), "   a b c d e\n"
                                     " 1 ~ ~ ~ ~ ~\n"
                                     " 2 ~ ~ ~ ~ ~\n"
                                     " 3 ~ ~ ~ ~ ~\n"
                                     " 4 ~ ~ ~ ~ ~\n"
                                     " 5 ~ ~ ~ ~ ~\n")

    def test_alternate_turns(self):
        self.game.alternate_turns(1, "a")
        ocean_pc = self.ocean_pc.get_board()
        self.assertEqual("   a b c d e\n"
                         " 1 . ~ ~ ~ ~\n"
                         " 2 ~ ~ ~ ~ ~\n"
                         " 3 ~ ~ ~ ~ ~\n" 
                         " 4 ~ ~ ~ ~ ~\n"
                         " 5 ~ ~ ~ ~ ~\n",str(ocean_pc))
