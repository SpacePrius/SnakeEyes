import snakeeyes

class TestDieBools():
    def test_dice_string(self):
        string = bool(snakeeyes.DiceString("28*15"))
        assert string is False
    def test_die(self):
        die = bool(snakeeyes.Die("28*15"))
        assert die is False
