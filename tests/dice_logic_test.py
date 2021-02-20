import snakeeyes
import pytest

def test_roll():
    return snakeeyes.Roll("1d20")

class TestMath():
    def test_add(self):
        return snakeeyes.Roll("1d20+5")
    def test_sub(self):
        return snakeeyes.Roll("1d20-5")
    def test_mult(self):
        return snakeeyes.Roll("1d20*5")
    def test_div(self):
        return snakeeyes.Roll("1d20/5")
    def test_raw(self):
        return snakeeyes.Roll("25*3")
    def test_parenth(self):
        return snakeeyes.Roll("(1d20+5)*20")

class TestOperators():
    def test_success(self):
        return snakeeyes.Roll("1d20>5")
    def test_explode(self):
        return snakeeyes.Roll("100d20x10")