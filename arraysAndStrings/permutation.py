# O(1) if the string lengths are different, and O(N) if the string lengths are the same.
def permutations(s1, s2):
    if len(s1) != len(s2):
        return False

    char_counts = {}

    for c in s1:
        if c in char_counts:
            char_counts[c] = char_counts[c] + 1
        else:
            char_counts[c] = 1

    for c in s2:
        if c in char_counts:
            char_counts[c] = char_counts[c] - 1

            if char_counts[c] < 0:
                return False
        else:
            return False

    return True


assert permutations('abcde', 'cabed') == True
assert permutations('abcde', 'abcde') == True
assert permutations('abcde', 'cbed') == False
assert permutations('abcde', 'abcxe') == False
print('Passed!')
