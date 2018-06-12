# Gregory Albert
# gja136
# 11158762
# CMPT 145 - L03

import TStack as Stack


def create():
    """

    Purpose

        creates an empty queue

    Return

        an empty queue

    """

    q2 = {}

    q2['e-stack'] = Stack.create()

    q2['d-stack'] = Stack.create()

    return q2


def is_empty(queue):
    """

    Purpose

        checks if the given queue has no data in it

    Pre-conditions:

        queue is a queue created by create()

    Return:

        True if the queue has no data, or false otherwise

    """

    # checking if both stacks are empty

    if Stack.is_empty(queue['e-stack']) and Stack.is_empty(queue['d-stack']):
        return True

    return False


def size(queue):
    """

    Purpose

        returns the number of data values in the given queue

    Pre-conditions:

        queue: a queue created by create()

    Return:

        The number of data values in the queue

    """

    # returning the size of two stacks combined

    return Stack.size(queue['e-stack']) + Stack.size(queue['d-stack'])


def enqueue(queue, value):
    """

    Purpose

        adds the given data value to the given queue

    Pre-conditions:

        queue: a queue created by create()

        value: data to be added

    Post-condition:

        the value is added to the queue

    Return:

        (none)

    """

    # removing all elements from d-stack (if exists) and pushing to e-stack

    while not Stack.is_empty(queue['d-stack']):
        Stack.push(queue['e-stack'], Stack.pop(queue['d-stack']))

    # pushing to the top of e-stack

    Stack.push(queue['e-stack'], value)


def dequeue(queue):
    """

    Purpose

        removes and returns a data value from the given queue

    Pre-conditions:

        queue: a queue created by create()

    Post-condition:

        the first value is removed from the queue

    Return:

        the first value in the queue

        """

    # removing all elements from e-stack (if exists) and pushing to d-stack

    while not Stack.is_empty(queue['e-stack']):
        Stack.push(queue['d-stack'], Stack.pop(queue['e-stack']))

    # removing and returning top element of d-stack, if not empty

    if not is_empty(queue):
        return Stack.pop(queue['d-stack'])

    return None


def peek(queue):
    """

    Purpose

        returns the value from the front of given queue without removing it

    Pre-conditions:

        queue: a queue created by create()

    Post-condition:

        None

    Return:

        the value at the front of the queue

    """

    while not Stack.is_empty(queue['e-stack']):
        Stack.push(queue['d-stack'], Stack.pop(queue['e-stack']))

    # returning (without removing) top element of d-stack, if not empty

    if not is_empty(queue):
        return Stack.peek(queue['d-stack'])

    return None


# main.py

import QueueTwo  # importing QueueTwo

# creating a QueueTwo object

queue2 = QueueTwo.create()

# enqueuing some numbers

QueueTwo.enqueue(queue2, 10)

QueueTwo.enqueue(queue2, 20)

QueueTwo.enqueue(queue2, 30)

# performing different operations

print('Size: ', QueueTwo.size(queue2))  # should display 3

print('Front element: ', QueueTwo.peek(queue2))  # 10

print('Queue: ', end=' ')  # printing the queue elements in a single line

while not QueueTwo.is_empty(queue2):
    print(QueueTwo.dequeue(queue2), end=' ')  # 10 20 30

print()  # blank line

print('Is empty now: ', QueueTwo.is_empty(queue2))  # True
