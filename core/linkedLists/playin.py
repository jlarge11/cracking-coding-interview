from linkedList import LinkedList

l = LinkedList()
n = l.add('Alpha')
n = n.add('Bravo')
n = n.add('Charlie')
n = n.add('Delta')

n = l.first()

while n :
    print(n.val)
    n = n.next

n = l.first() # Alpha
n = n.next    # Bravo
n.add('Bravo Bravo')

print('=========================================')

n = l.first()

while n :
    print(n.val)
    n = n.next

