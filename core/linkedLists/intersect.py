from linkedList import LinkedList

def intersect(l1, l2) :
    nodeSet = set()

    n1 = l1.firstNode
    n2 = l2.firstNode

    while n1 or n2 :
        if n1 :
            if n1 in nodeSet : return n1
            nodeSet.add(n1)
            n1 = n1.next

        if n2 :
            if n2 in nodeSet : return n2
            nodeSet.add(n2)
            n2 = n2.next

    return None

l1 = LinkedList(1, 2, 3)
l2 = LinkedList(4, 5, 6)

print('Before intersecting')
l1.print()
print('===')
l2.print()
print('===')
print(intersect(l1, l2))
print('===')
print(intersect(l2, l1))

print('After intersecting')
l2.lastNode.next = l1.firstNode

l1.print()
print('===')
l2.print()
print('===')

print(intersect(l1, l2).val)
print('===')
print(intersect(l2, l1).val)
