# O(N)
from core.collections import LinkedList


def delete_middle(n):
    prev = None
    current = n

    while(current.next):
        current.val = current.next.val
        prev = current
        current = current.next

    prev.remove_next()


def list_with_middle_node(which, *elements):
    middle_node = None

    l = LinkedList(*elements)
    current = l.head.next

    for i in range(len(elements)):
        if i == which:
            middle_node = current
            break

        current = current.next

    return middle_node, l


n, l = list_with_middle_node(
    3, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

delete_middle(n)

assert l.equals(LinkedList('a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j'))

print('Passed!')
