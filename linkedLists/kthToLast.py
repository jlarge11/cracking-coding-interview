from linkedList import LinkedList

# O(n)
def removeFronEndOffset(l, k) :
    size = 0
    n = l.first()

    while n :
        size += 1
        n = n.next

    n = l.head
    i = 0

    while n.next :
        if size - i - 1 == k :
            n.removeNext()
            return

        i += 1
        n = n.next

l = LinkedList()
n = l.addAtFront('Alpha')
n = n.add('Bravo')
n = n.add('Charlie')
n = n.add('Delta')
n = n.add('Echo')
n = n.add('Foxtrot')
n = n.add('Golf')

l.print()
removeFronEndOffset(l, 3)
print('==========================')
l.print()
