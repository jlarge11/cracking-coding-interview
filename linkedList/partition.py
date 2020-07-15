# O(N)
from core.collections import LinkedList


def partition(x, l):
    left = LinkedList()
    right = LinkedList()

    current = l.head

    while current:
        if current.val < x:
            left.add(current.val)
        else:
            right.add(current.val)

        current = current.next

    left.lastNode.next = right.head

    return left


assert partition(5, LinkedList(3, 7, 8, 1, 4, 5, 9)).equals(
    LinkedList(3, 1, 4, 7, 8, 5, 9))

assert partition(5, LinkedList(3, 7, 8, 1, 4, 9)).equals(
    LinkedList(3, 1, 4, 7, 8, 9))

print('Passed!')
