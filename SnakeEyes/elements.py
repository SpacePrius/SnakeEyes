"""Handles the Grammar of the document"""
import re
import logging

logger = logging.getLogger('dice.elements')


class DiceString():
    """
        Generates the dice string to put through the system

        Attributes
        ----------
        parsestring : Pattern
            Regex pattern to detect the various attributes of a dice roll

        quantity : int
            Number of times die must be rolled

        sides : int
            Number of sides a die has

    """
    parsestring = re.compile(r"(?P<quantity>\d*(?=d\d*))d(?P<sides>\d*)")

    def __init__(self, string):
        logger.debug("Initating DiceString")
        dice = self.parsestring.search(string)
        self.quantity = dice.group("quantity")
        self.sides = dice.group("sides")


class Operator():
    """
    Handles creating operators for use in rolls

    ...

    Attributes
    ----------
    char : str
        character for operand
    regex : str
        raw string, by default just detects the character

    Functions
    -------
    parse

    """
    char = None
    regex = rf"{char}"
    compiled = re.compile(regex)

    def parse(self, string):
        """
        Take a string and output its operator and operands
        """
        pass


class Roll():
    """
    Class that handles dice rolls using the rand function and regular expressions

    ...

    Attributes
    ----------
    string : str
        String to be processed

    """

    def __init__(self, string: str):
        self.string = string
        self.dice = DiceString(string)
        self.remainder = re.search(r"[^\dd].*", string)
