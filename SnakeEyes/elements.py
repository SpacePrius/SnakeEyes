"""Handles the Grammar of the document"""
import re
import logging
import random
import math
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


class Die():
    """
    Class that handles dice rolls using the rand function and regular expressions

    ...

    Attributes
    ----------
    string : str
        String to be processed

    """
    opparse = re.compile(r"([^\dd]\d*)")

    def __init__(self, string: str):
        self.string = string
        self.dice = DiceString(string)
        self.oplist = self.opparse.findall(string)


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
    parse - Take the string and show that its there
    evaluate - Blank method where the operator is processed

    """
    char = r""
    regex = rf"[{char}]"

    def __init__(self):
        pass

    def parse(self, string):
        """
        Take a string and output its operator and operands
        """
        compiled = re.compile(self.regex)
        return compiled.search(string).group

    def evaluate(self, dice):
        pass


class LeftHandOperator(Operator):
    """
    Operators that act on the object to the left, using the object on the right, inherits from Operator

    Attributes
    ----------
    operand : str
        The arguments taken by the operator

    """
    operand = r"\d*"

    def __init__(self):
        Operator.__init__(self)
        self.regex = rf"(?P<operator>[{self.char}])(?P<operand>{self.operand})"

    def parse(self, string):
        compiled = re.compile(self.regex)
        return compiled.search(string).groupdict()


class Successes(LeftHandOperator):

    """
    Takes an operand and calculates how many successes there have been
    """
    char = r">"

    def evaluate(self, opstring, results: list):
        dice_dict = {}
        logger.debug("Evaluating successes!")
        i = 0
        for d in results:
            if d >= int(self.parse(opstring)['operand']):
                dice_dict[i] = True
            else:
                dice_dict[i] = False
            i += 1

class Exploding(LeftHandOperator):
    """
    Takes an operand of explode threshold, and adds another die whenever the roll threshold is passed
    """

    char = r"x"

    def evaluate(self, die: Die, opstring: str, results: list):
        for d in results:
            if d >= int(self.parse(opstring)['operand']):
                # Roll another die, then check again if it is above operand, repeat until false
                pass
