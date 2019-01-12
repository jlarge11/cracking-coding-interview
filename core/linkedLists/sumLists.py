from linkedList import LinkedList

def nodeValueOrZero(n) :
    if not n : return 0
    return n.val

def safeNext(n) :
    if not n : return None
    return n.next

def sumLists(l1, l2) :
    l1Node = l1.firstNode
    l2Node = l2.firstNode
    result = LinkedList()
    carry = 0

    while l1Node or l2Node :
        digitSum = carry + nodeValueOrZero(l1Node) + nodeValueOrZero(l2Node)
        resultDigit = digitSum % 10
        carry = digitSum // 10

        result.add(resultDigit)
        l1Node = safeNext(l1Node)
        l2Node = safeNext(l2Node)

    if carry > 0 : result.add(carry)
    return result

def sumListsNormalOrder(l1, l2) :
    sums = []
    l1Node = l1.firstNode
    l2Node = l2.firstNode

    while l1Node or l2Node :
        sums.append(nodeValueOrZero(l1Node) + nodeValueOrZero(l1Node))

    for i, d in reversed(list(enumerate(sums))) :
        if d >= 10 and i > 0 :
            carry = d // 10
            d = d % 10
            sums[i - 1] += carry

    result = LinkedList(sums)
    oldFirstDigit = result.firstNode.val

    if oldFirstDigit >= 10 :
        newFirstDigit = oldFirstDigit // 10
        newSecondDigit = oldFirstDigit % 10
        newFirstNode = result.addAtFront(newFirstDigit)
        newFirstNode.next.val = newSecondDigit

    return result
        
l1 = LinkedList(7, 1, 6, 9)
l2 = LinkedList(5, 9, 3)
result = sumLists(l1, l2)
result.print()
