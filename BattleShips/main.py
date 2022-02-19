from domain.board import Board, Radar
from game.game import Game
from player.computer import Computer
from player.human import Human
from UIs.ui import UI
from repository.ocean import Ocean
from strategy.dumbStrat import BasicBot
from strategy.noStrat import NoStrategy
from validators.validators import Validators

if __name__ == '__main__':
    board = Board(10, 10)
    radar = Radar(10, 10)
    ocean_human = Ocean(board)
    ocean_pc = Ocean(radar)
    strategy = BasicBot()
    # strategy = NoStrategy()
    player1 = Human(board, radar)
    player2 = Computer(board, radar, strategy)
    # player2 = Human(board, radar)
    validators = Validators()
    game = Game(ocean_human, ocean_pc, player1, player2, validators)
    #
    # game.play()
    console = UI(game)
    console.play()
