class LinkedList :
    def __init__(self, *elements) :
        self.head = Node()
        self.lastNode = self.head
        for e in elements : self.add(e)
            
    def add(self, val) :
        newNode = Node(val)
        self.lastNode.next = newNode
        self.firstNode = self.head.next
        self.lastNode = self.lastNode.next
        return newNode

    def print(self) :
        n = self.firstNode

        while n :
            print(n.val)
            n = n.next
        

class Node :
    def __init__(self, val = None) :
        self.val = val
        self.next = None

    def add(self, val) :
        newNext = Node(val)
        oldNext = self.next
        newNext.next = oldNext
        self.next = newNext
        return newNext

    def removeNext(self) :
        oldNext = self.next
        if not oldNext : return
        newNext = oldNext.next
        self.next = newNext
