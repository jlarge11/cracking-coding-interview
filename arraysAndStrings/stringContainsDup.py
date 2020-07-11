# O(1) since function immediately returns True if string length is greater than 128.
def contains_dups(s):
    if len(s) > 128:
        return True

    chars = set()

    for c in s:
        if c in chars:
            return True

        chars.add(c)

    return False


print(contains_dups('alpha'))
print(contains_dups('bravo'))
