from linkedList import LinkedList

def findCircularNode(l) :
    n = l.firstNode
    nodes = set()

    while n :
        if n in nodes : return n
        nodes.add(n)
        n = n.next

    return None

l = LinkedList(1, 2, 3)
print(findCircularNode(l))
circularNode = l.add(4)
l.add(5)
l.add(6)
l.lastNode.next = circularNode
print(findCircularNode(l).val)
