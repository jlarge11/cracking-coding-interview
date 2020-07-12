# O(N)
from core.collections import LinkedList


def remove_dups(l):
    known_values = set()

    current = l.head
    known_values.add(current.val)

    while(current.next):
        if current.next.val in known_values:
            current.remove_next()
        else:
            known_values.add(current.next.val)
            current = current.next


def test(initial, expected):
    l = LinkedList(*initial)
    remove_dups(l)

    expected_list = LinkedList(*expected)

    assert expected_list.equals(l)


test([1, 3, 7, 3, 2, 1, 5], [1, 3, 7, 2, 5])
print('Passed!')
