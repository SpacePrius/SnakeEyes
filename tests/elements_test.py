import snakeeyes


class TestDieBools():
    def test_dice_string(self):
        """
        Set the string representation of a string.

        Args:
            self: (todo): write your description
        """
        string = bool(snakeeyes.Die("28*15"))
        assert string is False

    def test_die(self):
        """
        Set the test test.

        Args:
            self: (todo): write your description
        """
        die = bool(snakeeyes.DiceGroup("28*15"))
        assert die is False
