from exception.exceptions import ShipPlacementError


def check_order(a, b):
    """
    Function that swaps element to respect a < b
    :param a: any
    :param b: any
    :return: a and b in order
    """
    if a > b:
        return b, a
    return a, b


class Ocean:
    """
    Obj that represents the board and the ships placed.
    """
    def __init__(self, board):
        self.__board = board
        self.__ships = []

    def place_ship(self, ship):
        """
        Function that places a ship on the board.
        :param ship: ship to be added (object of type Ship)
        :raises: exception if the ship can't be spot because there already exist a ship there.
        """
        if ship.x1 == ship.x2:
            y1, y2 = check_order(ship.y1, ship.y2)
            y1_nr = ord(y1) - 97  # positioned -1
            y2_nr = ord(y2) - 97  # positioned -1
            for column in range(y1_nr, y2_nr + 1):
                j = chr(column + 97)
                if self.__board.get_value(ship.x1, j) != "~":
                    raise ShipPlacementError("Can't place the ship there!")
                self.__board.set_value(ship.x1, j, ship.id)

        elif ship.y1 == ship.y2:
            x1, x2 = check_order(ship.x1, ship.x2)
            for i in range(x1, x2 + 1):
                if self.__board.get_value(i, ship.y1) != "~":
                    raise ShipPlacementError("Can't place the ship there!")
                self.__board.set_value(i, ship.y1, ship.id)

        self.__ships.append(ship)

    def get_ship_status(self, ship):
        """
        Function to check whether the ship is sunk or not.
        :param ship: the ship to be checked (object of type Ship)
        :return: True if the ship is alive.
        False if sunk.
        """
        cells_sunk = 0
        if ship.x1 == ship.x2:
            no_cells = abs(ord(ship.y2) - ord(ship.y1)) + 1
            y1, y2 = check_order(ship.y1, ship.y2)
            y1 = ord(y1) - 97
            y2 = ord(y2) - 97
            for j in range(y1, y2+1):
                if self.__board.get_value(ship.x1, chr(j+97)) == "X":
                    cells_sunk += 1
            return (no_cells - cells_sunk) != 0

        if ship.y1 == ship.y2:
            no_cells = abs(ship.x2 - ship.x1) + 1
            x1, x2 = check_order(ship.x1, ship.x2)
            for i in range(x1, x2+1):
                if self.__board.get_value(i, ship.y1) == "X":
                    cells_sunk += 1
            return (no_cells - cells_sunk) != 0

    def get_board(self):
        return self.__board

    def get_ships(self):
        return self.__ships
