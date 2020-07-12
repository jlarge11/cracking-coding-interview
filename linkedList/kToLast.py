# O(N)
from core.collections import LinkedList


def k_to_last(l, k):
    trailer = l.head
    current = l.head

    for i in range(k - 1):
        current = current.next

    while(current.next):
        trailer = trailer.next
        current = current.next

    return trailer.val


assert k_to_last(LinkedList(1, 2, 3, 4, 5, 6, 7, 8), 3) == 6
assert k_to_last(LinkedList(1, 2, 3, 4, 5, 6, 7, 8), 1) == 8

print('Passed!')
