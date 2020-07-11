def is_palindrome_perm(s):
    trimmed_string_len = 0
    odd_chars = set()

    for c in s:
        if c != ' ':
            trimmed_string_len += 1

            if c in odd_chars:
                odd_chars.remove(c)
            else:
                odd_chars.add(c)

    if trimmed_string_len % 2 == 0:
        return len(odd_chars) == 0
    else:
        return len(odd_chars) == 1


assert is_palindrome_perm('abba')
assert is_palindrome_perm('aabb')
assert is_palindrome_perm('abb a')
assert is_palindrome_perm('abcba')
assert is_palindrome_perm('cabab')
assert is_palindrome_perm('a bcba')
assert not is_palindrome_perm('cabcabac')
print('Passed!')
