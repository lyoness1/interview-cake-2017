def find_unique_integer(integers):
    """
        >>> find_unique_integer([1, 2, 3, 4, 5, 1, 2, 3, 4])
        5
        >>> find_unique_integer([1, 2, 1, 3, 4, 3, 2, 5, 5])
        4
    """

    ids = 0
    for drone in integers:
        # XOR operator flips bit on if not seen, off if seen. 
        ids = ids ^ drone

    return int(ids)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
