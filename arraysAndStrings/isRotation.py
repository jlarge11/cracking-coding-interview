def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 += s1

    return s2 in s1


assert is_rotation('waterbottle', 'waterbottle')
assert is_rotation('waterbottle', 'erbottlewat')
assert not is_rotation('waterboxtxe', 'erbottlewat')
assert not is_rotation('xxxwaterbottle', 'erbottlewat')

print('Passed!')
