def reverse_words(phrase):
    """
        >>> reverse_words('find you will pain only go you recordings security the into if')
        'if into the security recordings you go only pain will you find'
    """
    words = phrase.split(' ')
    words.reverse()  # probably not in the spirit of this problem
    return ' '.join(words)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
