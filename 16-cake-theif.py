# (weight, value)
# weight, value >= 0

def max_duffel_bag_value(cake_types, capacity):
    """
        >>> cake_types = [(7, 160), (3, 90), (2, 15)]
        >>> capacity = 20
        >>> max_duffel_bag_value(cake_types, capacity)
        555
        >>> cake_tuples = [(3, 40), (5, 70)]
        >>> capacity    = 9
        >>> max_duffel_bag_value(cake_tuples, capacity)
        120
    """
    max_value_for_capacities = [0] * (capacity + 1)
    
    for weight in xrange(capacity+1):
        max_profit_at_weight = 0

        for cake_weight, cake_value in cake_types:
            if cake_weight <= weight:
                remainder = weight - cake_weight
                max_value_for_cake = (
                    cake_value + max_value_for_capacities[remainder]
                )
                max_profit_at_weight = max(
                    max_value_for_cake, max_profit_at_weight
                )

        max_value_for_capacities[weight] = max_profit_at_weight

    return max_value_for_capacities[capacity]

        

        


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"

