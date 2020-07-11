# O(N) where N is the length of the bigger string
def is_one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if (len(s1) >= len(s2)):
        bigger_string = s1
        smaller_string = s2
    else:
        bigger_string = s2
        smaller_string = s1

    bigger_string_index = 0
    has_already_edited = False

    for c in smaller_string:
        if c != bigger_string[bigger_string_index]:
            if has_already_edited:
                return False

            has_already_edited = True

            if len(smaller_string) != len(bigger_string):
                bigger_string_index += 1

        bigger_string_index += 1

    return True


assert is_one_away('pale', 'pale')
assert is_one_away('pale', 'ple')
assert is_one_away('pales', 'pale')
assert is_one_away('pale', 'bale')
assert not is_one_away('pale', 'bake')
print('Passed!')
