# O(1)
from core.collections import LinkedList


def delete_middle(n):
    n.val = n.next.val
    n.next = n.next.next


def list_with_middle_node(which, *elements):
    middle_node = None

    l = LinkedList(*elements)
    current = l.head

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
