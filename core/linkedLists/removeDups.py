from linkedList import LinkedList

# O(n)
def removeDups(l) :
    n = l.first()
    valuesAlreadySeen = {n.val}

    while n and n.next :
        if n.next.val in valuesAlreadySeen :
            n.removeNext()
        else :
            valuesAlreadySeen.add(n.next.val)
            n = n.next

# O(n^2)
def removeDupsWithoutBuffer(l) :
    n = l.first()

    while n and n.next :
        possibleDup = n

        while possibleDup :
            if possibleDup.next and possibleDup.next.val == n.val :
                possibleDup.removeNext()
            else :
                possibleDup = possibleDup.next

        n = n.next

l = LinkedList()
n = l.addAtFront('Alpha')
n = n.add('Bravo')
n = n.add('Charlie')
n = n.add('Delta')
n = n.add('Echo')
n = n.add('Bravo')

l.print()
print('=====================')
removeDupsWithoutBuffer(l)
l.print()
