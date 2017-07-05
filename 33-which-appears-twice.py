def find_which_appears_twice(arr):
    """
        >>> find_which_appears_twice([1, 2, 3, 3, 4, 5])
        3
        >>> find_which_appears_twice([3, 4, 5, 2, 1, 4])
        4
    """
    # Because know lengs, use math: sum = (n^2 + n) / 2
    n = len(arr) - 1
    expected_sum = (n*n + n) / 2
    actual_sum = 0
    for num in arr:
        actual_sum += num

    return actual_sum - expected_sum



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
