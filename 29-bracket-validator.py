def is_properly_nested(phrase):
    """
        >>> is_properly_nested('{[]()}')
        True
        >>> is_properly_nested('{[(])}')
        False
        >>> is_properly_nested('{[}')
        False
    """
    OPENERS = ['{', '[', '(']
    CLOSERS = ['}', ']', ')']
    seen = []

    for char in phrase:
        if char in OPENERS:
            seen.append(char)
        elif char in CLOSERS:
            if not seen:
                return False
            opener = seen[-1]
            if OPENERS.index(opener) == CLOSERS.index(char):
                seen.pop()

    if not seen:
        return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
