from linkedList import LinkedList

def partition(l, x) :
    lower = LinkedList()
    higher = LinkedList()

    n = l.firstNode

    while n :
        if n.val < x :
            lower.add(n.val)
        else :
            higher.add(n.val)

        n = n.next

    lower.lastNode.next = higher.firstNode
    return lower

l = LinkedList(3, 5, 8, 5, 10, 2, 1)

l.print()
print('=================================')
p = partition(l, 5)
p.print()
