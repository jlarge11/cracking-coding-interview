# Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2).  That is, 617 + 295
# Output: 2 -> 1 -> 9.  That is, 912
from core.collections import LinkedList


def sum_lists(list1, list2):

    current1 = l.head
    current2 = l.head
    result = LinkedList(0)
    result_current = result.head

    while current1.next or current2.next:
        current1 = current1.next
        current2 = current1.next
        val1 = 0
        val2 = 0

        if current1:
            val1 = current1.val

        if current2:
            val2 = current2.val

        mini_sum = val1 + val2
        carry = mini_sum / 10
        mini_val = mini_sum % 10

        result.add(mini_val)


assert partition(5, LinkedList(3, 7, 8, 1, 4, 5, 9)).equals(
    LinkedList(3, 1, 4, 7, 8, 5, 9))

assert partition(5, LinkedList(3, 7, 8, 1, 4, 9)).equals(
    LinkedList(3, 1, 4, 7, 8, 9))

print('Passed!')
