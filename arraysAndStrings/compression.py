# O(N) where N is the length of the string
# Note:  I used a char[] to avoid string concatenation which is O(N^2), or at least it is in Java.
def compress(s):
    compressed = [''] * len(s)
    compressed_index = 0
    prev = ''
    repeat_count = 0

    for c in s:

        if c != prev:
            prev = c

            if compressed_index > 0:
                compressed[compressed_index] = str(repeat_count)
                compressed_index += 1

                if compressed_index == len(compressed):
                    return s

                repeat_count = 0

            compressed[compressed_index] = c
            compressed_index += 1

            if compressed_index == len(compressed):
                return s

        repeat_count += 1

    compressed[compressed_index] = str(repeat_count)
    compressed_index += 1

    if compressed_index == len(compressed):
        return s

    return ''.join(compressed)


assert(compress('aabcccccaaa') == 'a2b1c5a3')
assert(compress('aabccccca') == 'a2b1c5a1')
assert(compress('aaaa') == 'a4')
assert(compress('justin') == 'justin')
assert(compress('a') == 'a')
print('Passed!')
