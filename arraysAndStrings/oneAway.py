# Runtime is O(n)

def oneAway(s1, s2) :
    lengthDifference = len(s1) - len(s2)
    if abs(lengthDifference) > 1 : return False

    numberOfDifferences = 0

    if lengthDifference >= 0 :
        smallerString = s2
        biggerString = s1
    else :
        smallerString = s1
        biggerString = s2

    six = 0
    for bix, c in enumerate(biggerString) :
        if six >= len(smallerString) or c != smallerString[six] :
            numberOfDifferences += 1
            if lengthDifference == 0 : six += 1
        else :
            six += 1

        if numberOfDifferences > 1 :
            return False

    return numberOfDifferences <= 1

assert     oneAway('pale', 'pale')
assert     oneAway('pale', 'paxe')
assert not oneAway('pale', 'pxxe')
assert     oneAway('pale', 'paxle')
assert not oneAway('pale', 'paxlx')
assert     oneAway('pale', 'palex')
assert not oneAway('pale', 'paleasdfasdf')

assert     oneAway('pale', 'pale')
assert     oneAway('paxe', 'pale')
assert not oneAway('pxxe', 'pale')
assert     oneAway('paxle', 'pale')
assert not oneAway('paxlx', 'pale')
assert     oneAway('palex', 'pale')
assert not oneAway('paleasdfasdf', 'pale')

print('Done')
