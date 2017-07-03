"""
    >>> a = LinkedListNode('A')
    >>> b = LinkedListNode('B')
    >>> c = LinkedListNode('C')
    >>> a.next = b
    >>> b.next = c
    >>> a.print_list()
    ['A', 'B', 'C']
    >>> delete_node(b)
    >>> a.print_list()
    ['A', 'C']
"""
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_list(self):
        values = []
        curr_node = self
        while curr_node:
            values.append(curr_node.value)
            curr_node = curr_node.next
        print values

def delete_node(node):
    # Doesn't really work for last node
    # External pointers will be wonky, node will dangle as garbage as result
    if not node.next:
        node = None

    node.value = node.next.value
    node.next = node.next.next


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
