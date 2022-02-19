from domain.ship import Ship
from exception.exceptions import StrikeError
from player.human import Human


class Game:
    def __init__(self, ocean1, ocean2, player1, player2, validator):
        """
        :param ocean: The game board on which the ships are placed
        :param player1: The human player
        :param player2: The computer
        """
        self.__player_h = player1
        self.__ocean_h = ocean1
        self.__ocean_c = ocean2
        self.__player_c = player2
        self.__validator = validator

    def get_second_coordinates(self, line, column, orientation, dimension):
        """
        Calculates the ending coordinates given the starting ones, orientation and the size
        :param line: (x1), the line corresponding to the starting coordinates of the ship, int
        :param column: (y1), the column corresponding to the starting coordinates of the ship, int
        :param orientation: vertical or horizontal, char ("v" or "h")
        :param dimension: integer representing the size of a ship
        :return: x2, y2 in this order, representing the new coordinates
        """
        if orientation == "v":
            return line + dimension - 1, column
        return line, chr(ord(column) + dimension - 1)

    def place_boat_human(self, line, column, orientation, ship_id, dimension):
        """
        Places a ship on the human board.
        :param line: (x1), the line corresponding to the starting coordinates of the ship, int
        :param column: (y1), the column corresponding to the starting coordinates of the ship, int
        :param orientation: vertical or horizontal, char ("v" or "h")
        :param ship_id: int from [0, 9] representing the id of a ship, which will be writen on the board
        :param dimension: integer representing the size of a ship
        :raises: validation exception if the data got is invalid
        """
        x1 = line
        y1 = column
        self.__validator.validate_orientation(orientation)
        x2, y2 = self.get_second_coordinates(line, column, orientation, dimension)
        ship = Ship(x1, y1, x2, y2, ship_id)
        self.__validator.validate(ship)
        self.__ocean_h.place_ship(ship)

    def place_boat_pc(self, line, column, orientation, ship_id, dimension):
        """
        Places a ship on the computer board.
        :param line: (x1), the line corresponding to the starting coordinates of the ship, int
        :param column: (y1), the column corresponding to the starting coordinates of the ship, int
        :param orientation: vertical or horizontal, char ("v" or "h")
        :param ship_id: int from [0, 9] representing the id of a ship, which will be writen on the board
        :param dimension: integer representing the size of a ship
        """
        x1 = line
        y1 = column
        x2, y2 = self.get_second_coordinates(line, column, orientation, dimension)
        ship = Ship(x1, y1, x2, y2, ship_id)
        self.__ocean_c.place_ship(ship)

    def __move(self, player, line, column):
        """
        :return: True if the game is over
                 False if not
        """
        if type(player) is Human:
            self.__validator.validate_strike(line, column)
        player.strike(line, column)

        if self.__game_over(player):
            return True
        return False

    def alternate_turns(self, line, column):
        # todo: documentation
        if self.__move(self.__player_h, line, column):
            return True, 0
        if self.__move(self.__player_c, line, column):
            return True, 1
        return False, 2

    def __game_over(self, player):
        """
        :param player:
        :return: True -> game is over
        """
        if type(player) is Human:
            ships = self.__ocean_c.get_ships()
            for ship in ships:
                # print(self.__ocean_c.get_ship_status(ship))
                if self.__ocean_c.get_ship_status(ship):
                    return False
            return True

        else:
            ships = self.__ocean_h.get_ships()
            for ship in ships:
                # print(self.__ocean_h.get_ship_status(ship))
                if self.__ocean_h.get_ship_status(ship):
                    print(self.__ocean_h.get_ship_status(ship))
                    return False
            return True

    def get_ocean(self):
        """
        :return: PLayer's board
        """
        return self.__ocean_h.get_board()

    def get_radar(self):
        """
        :return: Computer's board formatted so that you can't see the ships
        """
        return self.__ocean_c.get_board()

    def get_id_for_cell(self):
        pass