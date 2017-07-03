def reverse_string_in_place(str):
    """
        >>> reverse_string_in_place('Hello how are you')
        'uoy era woh olleH'
    """
    chars = list(str)

    left_idx = 0
    right_idx = len(str) - 1

    while right_idx > left_idx:
        temp = chars[left_idx]
        chars[left_idx] = chars[right_idx]
        chars[right_idx] = temp
        right_idx -= 1
        left_idx += 1

    return ''.join(chars)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
