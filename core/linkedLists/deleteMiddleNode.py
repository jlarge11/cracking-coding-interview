from linkedList import LinkedList

# O(n)
def delete(n) :
    runner = n.next

    while True :
        n.val = runner.val
        if not runner.next :
            n.next = None
            return

        n = n.next
        runner = runner.next

l = LinkedList()
n = l.addAtFront('Alpha')
n = n.add('Bravo')
n = n.add('Charlie')
n = n.add('Delta')
n = n.add('Echo')
n = n.add('Foxtrot')
n = n.add('Golf')
n = n.add('Hotel')
toRemove = n
n = n.add('India')

l.print()
print('=================================')
delete(toRemove)
l.print()
