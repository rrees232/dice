from dice import Die

def test_valid_roll():
    """ Test that a die roll is valid. """

    # Intialise a standard, six-sided die.
    die = Die()

    # Roll the die.
    roll = die.roll()

    # Check that the value is valid.
    assert roll > 0 and roll < 7
