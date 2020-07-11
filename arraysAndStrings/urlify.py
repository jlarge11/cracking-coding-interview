# O(N) where N is the length of the string passed in.
def urlify(s, length):
    result_index = len(s) - 1

    for original_index in reversed(range(length)):
        if s[original_index] == ' ':
            s[result_index] = '0'
            s[result_index - 1] = '2'
            s[result_index - 2] = '%'

            result_index -= 3
        else:
            s[result_index] = s[original_index]
            result_index -= 1


def test(s, length, expected):
    chars = list(s)
    urlify(chars, length)
    actual = ''.join(chars)
    print(f's = {s}; expected = {expected}; actual = {actual}')
    assert expected == actual


test('Mr John Smith    ', 13, 'Mr%20John%20Smith')
test('a   b     c                ', 11, 'a%20%20%20b%20%20%20%20%20c')
test('MrJohnSmith', 11, 'MrJohnSmith')
print('Passed!')
