"""
    >>> a = LinkedListNode("Angel Food")
    >>> b = LinkedListNode("Bundt")
    >>> c = LinkedListNode("Cheese")
    >>> d = LinkedListNode("Devil's Food")
    >>> e = LinkedListNode("Eccles")
    >>> a.next = b
    >>> b.next = c
    >>> c.next = d
    >>> d.next = e
    >>> get_kth_to_last_node(a, 2)
    "Devil's Food"
"""
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def get_kth_to_last_node(start_node, k):
    kth_to_last_node = start_node
    end_node = start_node

    for i in xrange(k):
        if not end_node.next:
            return "List not long enough"
        end_node = end_node.next

    while end_node:
        end_node = end_node.next
        kth_to_last_node = kth_to_last_node.next

    return kth_to_last_node.value



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
