# Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2).  That is, 617 + 295
# Output: 2 -> 1 -> 9.  That is, 912
# O(N)
from core.collections import LinkedList


def sum_lists(list1, list2):
    current1 = list1.head
    current2 = list2.head
    result = LinkedList()

    carry = 0

    while current1 or current2 or carry:
        unit_val = 0

        if current1:
            unit_val += current1.val
            current1 = current1.next

        if current2:
            unit_val += current2.val
            current2 = current2.next

        unit_val += carry

        carry = unit_val // 10
        unit_val %= 10

        result.add(unit_val)

    return result


assert sum_lists(LinkedList(7, 1, 6), LinkedList(
    5, 9, 2)).equals(LinkedList(2, 1, 9))

assert sum_lists(LinkedList(7, 1, 6), LinkedList(
    5, 9, 8)).equals(LinkedList(2, 1, 5, 1))

print('Passed!')
