# O(N)
from core.collections import LinkedList


def partition(x, l):
    left = LinkedList()
    right = LinkedList()

    current = l.head

    while current.next:
        current = current.next

        if current.val < x:
            left.add(current.val)
        else:
            right.add(current.val)

    left.lastNode.next = right.head.next

    return left


assert partition(5, LinkedList(3, 7, 8, 1, 4, 5, 9)).equals(
    LinkedList(3, 1, 4, 7, 8, 5, 9))

assert partition(5, LinkedList(3, 7, 8, 1, 4, 9)).equals(
    LinkedList(3, 1, 4, 7, 8, 9))

print('Passed!')
