"""Handles the Grammar of the document"""
import re
import logging

logger = logging.getLogger('dice.elements')

class StringCompiler():
    parsestring = None
    

class DiceString(StringCompiler):
    """
        Generates the dice string to put through the system
    """
    parsestring = re.compile(r"(?P<quantity>\d*(?=d\d*))d(?P<sides>\d*)")
    def __init__(self, string):
        logger.debug("Initating DiceString")
        dice = self.parsestring.search(string)
        self.quantity = dice.group("quantity")
        self.sides = dice.group("sides")



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
        logger.info("Roll Created!")
        self.string = string
        logger.info("Roll string" + str(self.string))
        mathstring = self.mathparse.findall(string)
        tempstring = ""
        for m in mathstring:
            tempstring = tempstring + str(m)
        self.mathstring = tempstring
        self.opstring = self.opparse.search(string)

class Operator():
    """
    Handles creating operators for use in rolls
    """
    char: str = None    
    def __init__(self, roll: Roll):
        self.roll = roll

    def operate(self, parse):
        pass

    def parse(self, char):
        operator = re.compile(rf"{char}")
        operator.search(self.roll.opstring)



    