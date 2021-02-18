"""Handles the actual logic of dice rolls"""
import math
import random
import re
import logging

from elements import Die, Exploding, Successes

logging.getLogger('snakeeyes.dicelogic')
class Roll():
    """A class which takes a string and outputs a dice roll

    Parameters
    ----------
    string : str
        The input string

    Attributes
    ----------
    dicer_regex : str
        Regex showing how to extract just the dice string from an object
    op_dict : dict
        dictionary containing the characters of an operator, and the assosciated class
    die : Die
        Dice roll using string input
    results : list
        List of results from dice rolled
    total : int
        The total of all dice rolled

    Methods
    -------
    roll
    """
    dice_regex = re.compile(r"\d*d\d*(?:[^d\d\(\)+\-\*/]\d*)*")

    def roll(self, die: Die):
        """Takes Die object and returns a tuple containing a list of results, and a total of of all rolls."""
        dice_array = []
        for i in range(die.dice.quantity):
            dice_array.append(math.ceil(random.random() * die.dice.sides))
        dice_total = 0
        for r in dice_array:
            dice_total += r
        return (dice_array, dice_total)

    __op_queue = []
    op_results = []

    def __init__(self, string: str):
        self.string = string
        self.die = Die(string)
        roll = self.roll(self.die)
        self.results = roll[0]
        self.total = roll[1]
        self.result_string = self.dice_regex.sub(f"{self.total}", string)
        self.eval_string = None 
        op_dict = {
            ">": Successes,
            "x": Exploding,
        }
        for o in self.die.operators:
            try:
                self.__op_queue.append(op_dict[o])
            except KeyError:
                continue
        for o in self.__op_queue:
            try:
                # Fix this later, opstring needs to be completely reworked. 
                # My head hurts atm and I need to get this crap fixed
                self.op_results.append(op_dict[o].evaluate(self, self.string))
            except KeyError:
                continue
