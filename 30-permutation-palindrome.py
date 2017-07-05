# Permutation: same letters
# Palindrome: same forwards as backwards

from collections import defaultdict

def is_permutation_a_palindrome(word):
    """
        >>> is_permutation_a_palindrome('civic')
        True
        >>> is_permutation_a_palindrome('ivicc')
        True
        >>> is_permutation_a_palindrome('civil')
        False
        >>> is_permutation_a_palindrome('livci')
        False
    """
    letter_counts = defaultdict(int)
    for char in word:
        letter_counts[char] += 1

    singles = 0
    for count in letter_counts.values():
        if count % 2 == 1:
            singles += 1

    return singles <= 1


def try_again(word):
    """
        >>> try_again('civic')
        True
        >>> try_again('ivicc')
        True
        >>> try_again('civil')
        False
        >>> try_again('livci')
        False
    """
    chars = set()
    for char in word:
        if char in chars:
            chars.remove(char)
        else:
            chars.add(char)

    return len(chars) <= 1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
