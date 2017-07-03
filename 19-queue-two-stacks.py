# Queue: First in, first out
# Stack: First in, last out

class Queue:
    def __init__(self):
        stack_1 = []
        stack_2 = []

    def enqueue(self, value):
        stack_1.append(value)

    def dequeue(self):
        if stack_2:
            return stack_2.pop()

        while stack_1:
            stack_2.append(stack_1.pop())

        return stack_2.pop()

"""
    >>> queue = Queue()
    >>> queue.enqueue('A')
    >>> queue.enqueue('B')
    >>> queue.enqueue('C')
    >>> queue.dequeue()
    'A'
    >>> queue.dequeue()
    'B'
    >>> queue.enqueue('D')
    >>> queue.enqueue('E')
    >>> queue.enqueue('F')
    >>> queue.dequeue()
    'C'
    >>> queue.dequeue()
    'D'
"""

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n\nALL TESTS PASSED!!\n\n"
