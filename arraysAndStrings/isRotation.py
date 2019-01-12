def isRotation(s1, s2) :
    if len(s1) != len(s2) : return False
    s2Times2 = s2 + s2
    return s1 in s2Times2

assert(isRotation('waterbottle', 'erbottlewat'))
assert(not isRotation('waterbottle', 'erboxxlewat'))
assert(not isRotation('waterttle', 'erbottlewat'))
print('Done')
