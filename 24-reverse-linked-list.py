"""
    >>> a = LinkedListNode('A')
    >>> b = LinkedListNode('B')
    >>> c = LinkedListNode('C')
    >>> a.next = b
    >>> b.next = c
    >>> a.print_list()
    ['A', 'B', 'C']
    >>> reverse_list(a)
    >>> c.print_list()
    ['C', 'B', 'A']
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

def reverse_list(head):
    if not head:
        return "Empty List"

    if not head.next: 
        return head

    curr_node = head
    next_node = curr_node.next
    curr_node.next = None

    while next_node:
        new_node = next_node.next
        next_node.next = curr_node
        curr_node = next_node
        next_node = new_node

    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
