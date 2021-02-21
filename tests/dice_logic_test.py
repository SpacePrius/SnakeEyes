import snakeeyes


def test_roll():
    """
    Test whether the test

    Args:
    """
    return snakeeyes.Roll("1d20")


class TestMath():
    def test_add(self):
        """
        Returns the test test for the test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("1d20+5")

    def test_sub(self):
        """
        Returns the test sub - test test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("1d20-5")

    def test_mult(self):
        """
        Return the test test test test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("1d20*5")

    def test_div(self):
        """
        Return the test test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("1d20/5")

    def test_raw(self):
        """
        Returns raw test test test test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("25*3")

    def test_parenth(self):
        """
        Return the test test test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("(1d20+5)*20")


class TestOperators():
    def test_success(self):
        """
        Return the test test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("1d20>5")

    def test_explode(self):
        """
        Return the test test.

        Args:
            self: (todo): write your description
        """
        return snakeeyes.Roll("100d20x10")
