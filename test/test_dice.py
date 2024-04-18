def test_always_valid_roll():
    """ Test that a die roll is "always" valid. """

    # Intialise a standard, six-sided die.
    die = Die()

    # Roll the die lots of times.
    for i in range(10000):
        roll = die.roll()

        # Check that the value is valid.
        assert roll > 0 and roll < 7
def test_valid_roll():
    """ Test that a die roll is valid. """

    # Intialise a standard, six-sided die.
    die = Die()

    # Roll the die.
    roll = die.roll()

    # Check that the value is valid.
    assert roll > 0 and roll < 7


def test_double_roll():
    pass


def prob_double_roll(x, n):
    """
    Expected probabilities for the sum of two dice.
    """
    # For two n-sided dice, the probability of two rolls summing to x is
    # (n − |x−(n+1)|) / n^2, for x = 2 to 2n.

    return (n - abs(x - (n + 1))) / n ** 2
