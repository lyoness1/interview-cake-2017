def all_permutations(word):
    """
        >>> all_permutations('cat')
        set(['atc', 'tac', 'cat', 'cta', 'act', 'tca'])
    """
    if len(word) == 1:
        return set(word)

    first_char = word[0]
    other_chars = word[1:]

    smaller_perms = all_permutations(other_chars)
    all_perms = set()

    for smaller_perm in smaller_perms:
        for i in xrange(len(word)):
            new_combo = smaller_perm[:i] + first_char + smaller_perm[i:]
            all_perms.add(new_combo)
    
    return all_perms


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
