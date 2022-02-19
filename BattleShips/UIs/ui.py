import random

from exception.exceptions import ShipPlacementError, ValidationException, StrikeError


class UI:
    def __init__(self, game):
        self.__game = game

    def set_up_boats_human(self):
        game_ships = {
            "0": 2,
            "1": 2,
            "2": 2,
            "3": 2,
            "4": 3,
            "5": 3,
            "6": 3,
            "7": 4,
            "8": 4,
            "9": 5
        }
        for piece in game_ships:
            ok = False
            while not ok:
                self.print_human_board()
                print(f"This ship has length {game_ships[piece]}! ")
                try:
                    line = int(input("Enter the line: "))
                    column = input("Enter the column: ")
                    orientation = input("Enter the orientation (press h or v): ")
                    ship_id = piece
                    dimension = game_ships[piece]

                    self.__game.place_boat_human(line, column, orientation, ship_id, dimension)
                    ok = True
                except ValidationException as ve:
                    print(ve)
                except ValueError as ve:
                    # if str(ve) == f"invalid literal for int() with base 10: '{line}'":
                    print("Line must be an integer between 1 and 10!")
                except ShipPlacementError as spe:
                    print(spe)
                except TypeError as te:
                    if str(te) == f"ord() expected a character, but string of length {len(column)} found":
                        print("Column must be a character between 'a' and 'j'")
                    else:
                        print(te)

    def set_up_boats_computer(self):
        """
        game_ships = {
            "0": 2,
            "1": 2,
            "2": 2,
            "3": 2,
            "4": 3,
            "5": 3,
            "6": 3,
            "7": 4,
            "8": 4,
            "9": 5
        }
        for piece in game_ships:
            ok = False
            while not ok:
                line = random.randint(1, 10)
                column = random.choice('abcdefghij')
                orientation = random.choice('vh')
                ship_id = piece
                dimension = game_ships[piece]
                try:
                    self.__game.place_boat_pc(line, column, orientation, ship_id, dimension)
                    ok = True
                except ShipPlacementError:
                    pass
        """
        # todo: different everytime
        self.__game.place_boat_pc(1, "a", "h", 3, 2)
        # self.__game.place_boat_pc(1, "d", "v", 4, 3)
        # self.__game.place_boat_pc(1, "g", "h", 7, 4)
        self.__game.place_boat_pc(3, "a", "v", 8, 4)
        # self.__game.place_boat_pc(3, "f", "h", 5, 3)
        # self.__game.place_boat_pc(3, "j", "v", 0, 2)
        # self.__game.place_boat_pc(8, "a", "h", 1, 2)
        # self.__game.place_boat_pc(6, "f", "v", 2, 2)
        # self.__game.place_boat_pc(6, "j", "v", 6, 3)
        # self.__game.place_boat_pc(10, "e", "h", 9, 5)

    def set_up_default(self):
        self.__game.place_boat_human(1, "a", "h", 3, 2)
        # self.__game.place_boat_human(1, "d", "v", 4, 3)
        # self.__game.place_boat_human(1, "g", "h", 7, 4)
        self.__game.place_boat_human(3, "a", "v", 8, 4)
        # self.__game.place_boat_human(3, "f", "h", 5, 3)
        # self.__game.place_boat_human(3, "j", "v", 0, 2)
        # self.__game.place_boat_human(8, "a", "h", 1, 2)
        # self.__game.place_boat_human(6, "f", "v", 2, 2)
        # self.__game.place_boat_human(6, "j", "v", 6, 3)
        # self.__game.place_boat_human(10, "e", "h", 9, 5)

    def print_human_board(self):
        board = self.__game.get_ocean()
        print(board)

    def print_radar(self):
        radar = self.__game.get_radar()
        print(radar)

    def read_the_data(self):
        while True:
            print("Press 1 for a default set up\n"
                  "Press 2 to place the ships yourself")
            mode = input(">>>")
            if mode == "1":
                self.set_up_default()
                self.print_human_board()
                self.set_up_boats_computer()
                # self.print_radar()
                break
            elif mode == "2":
                self.set_up_boats_human()
                self.print_human_board()
                self.set_up_boats_computer()
                # self.print_radar()
                break
            else:
                print("There is no such option!")

    def play(self):
        self.read_the_data()
        while True:
            try:
                self.print_radar()
                print("Enter the coordinates for the attack, commander!")
                line = int(input("Line: "))
                column = input("Column: ")
                game_status, winner = self.__game.alternate_turns(line, column)
                self.print_human_board()
                if game_status:
                    if winner == 0:
                        print("Victory! You won commander!")
                        break
                    elif winner == 1:
                        print("Defeat! You lost commander!")
                        break
            except ValidationException as ve:
                print(ve)
            except StrikeError as se:
                print(se)
            except ValueError as ve:
                print("Please enter a valid number")
            except TypeError as te:
                print(te)
