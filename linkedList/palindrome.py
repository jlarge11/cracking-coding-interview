# Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2).  That is, 617 + 295
# Output: 2 -> 1 -> 9.  That is, 912
from core.collections import LinkedList


def is_palindrome(l):
    array = []

    current = l.head

    while current:
        array.append(current.val)
        current = current.next

    length = len(array)

    for i, e in enumerate(array):
        if i <= length and e != array[length - i - 1]:
            return False

    return True


assert is_palindrome(LinkedList(1, 2, 3, 2, 1))
assert is_palindrome(LinkedList(1, 2, 3, 4, 3, 2, 1))

assert not is_palindrome(LinkedList(1, 2, 3, 4, 1))
assert not is_palindrome(LinkedList(1, 2, 3, 4, 3, 5, 1))

print('Passed!')
