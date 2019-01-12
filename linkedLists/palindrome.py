from linkedList import LinkedList

# 2n = O(n)
def isPalindrome(l) :
    n = l.firstNode
    a = []

    while n :
        a.append(n.val)
        n = n.next

    n = l.firstNode
    for i, e in enumerate(reversed(a)) :
        if e != n.val : return False
        n = n.next

    return True;

print(isPalindrome(LinkedList(1)))
print(isPalindrome(LinkedList(1, 2, 3, 2, 1)))
print(isPalindrome(LinkedList(1, 2, 2, 1)))
print(isPalindrome(LinkedList(1, 2, 3, 4)))
print(isPalindrome(LinkedList(1, 2, 3, 4, 5)))
