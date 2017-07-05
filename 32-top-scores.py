# With highest score, can initialize a histogram of scores to keep O(n)

def sort_scores(unsorted_scores, highest_possible_score):
    """
        >>> unsorted_scores = [37, 89, 41, 65, 91, 53]
        >>> highest_possible_score = 100
        >>> sort_scores(unsorted_scores, highest_possible_score)
        [37, 41, 53, 65, 89, 91]
    """
    score_counts = [0] * (highest_possible_score + 1)
    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []
    for idx, count in enumerate(score_counts):
        if count > 0:
            sorted_scores.append(idx)

    return sorted_scores

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
