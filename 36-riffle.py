def is_riffle(deck, firsthalf, secondhalf):
    """Returns True is deck is a single riffle of first and second halves
        >>> is_riffle([1, 2, 4, 3, 5, 6], [1, 2, 3], [4, 5, 6])
        True
        >>> is_riffle([1, 3, 4, 5, 6, 2], [1, 2, 3], [4, 5, 6])
        False
    """
    while firsthalf or secondhalf:
        top_card = deck.pop()
        if top_card == firsthalf[-1]:
            firsthalf.pop()
        elif top_card == secondhalf[-1]:
            secondhalf.pop()
        else:
            return False

    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
