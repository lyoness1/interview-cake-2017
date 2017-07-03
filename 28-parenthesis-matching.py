def find_matching_parenthesis_index(phrase, start_idx):
    """
        >>> phrase = "find (matching (paren)) here."
        >>> find_matching_parenthesis_index(phrase, 5)
        22
        >>> find_matching_parenthesis_index("h(ello", 2)
        'Not closed'
    """
    openers = [start_idx]
    for i in xrange(start_idx+1, len(phrase)):
        if phrase[i] == '(':
            openers.append(i)
        if phrase[i] == ')':
            if openers[-1] == start_idx:
                return i
            openers.pop()
    return "Not closed"

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
