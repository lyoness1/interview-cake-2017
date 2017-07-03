"""
    >>> a = LinkedListNode('A')
    >>> b = LinkedListNode('B')
    >>> c = LinkedListNode('C')
    >>> a.next = b
    >>> b.next = c
    >>> has_cycle(a)
    False
    >>> has_cycle_smaller(a)
    False
    >>> c.next = a
    >>> has_cycle(a)
    True
    >>> has_cycle_smaller(a)
    True
"""
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(start_node):
    seen = set()
    curr_node = start_node
    while curr_node:
        if curr_node in seen:
            return True
        seen.add(curr_node)
        curr_node = curr_node.next
    return False

def has_cycle_smaller(start_node):
    slow = start_node
    fast = start_node

    while fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
