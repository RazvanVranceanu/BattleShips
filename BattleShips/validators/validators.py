from exception.exceptions import ValidationException


def is_char(a):
    """
    Checks if a given char is a lower case letter
    :param a: char
    :return: True if it is, False if it's not
    """
    if len(a) == 1 and "a"<=a<="z":
        return True
    return False


class Validators:
    def validate(self, ship):
        """
        Validates the data used for creating a ship
        :param ship: object if type Ship
        :raises ValidationException: if the data is incorrect
        """
        errors = ""
        if not self.__check_x(ship.x1) or not self.__check_x(ship.x2):
            errors += "Invalid line!\n"
        if not self.__check_y(ship.y1) or not self.__check_y(ship.y2):
            errors += "Invalid column!\n"
        if len(errors) > 0:
            raise ValidationException(errors)

    def validate_strike(self, line, column):
        """
        Validate the coordinates of a strike
        :param line: int [0, 10]
        :param column: char ['a', 'j']
        :raises ValidationException: if the data is incorrect
        """
        errors = ""
        if not self.__check_x(line):
            errors += "Invalid line!\n"
        if not self.__check_y(column):
            errors += "Invalid column!\n"
        if len(errors) > 0:
            raise ValidationException(errors)

    def __check_x(self, x):
        if x < 1 or x > 10:
            return False
        return True

    def __check_y(self, y):
        if not is_char(y) or y > "j":
            return False
        return True

    def validate_orientation(self, letter):
        if letter != "v" and letter != "h":
            raise ValidationException("Invalid orientation!\n")
