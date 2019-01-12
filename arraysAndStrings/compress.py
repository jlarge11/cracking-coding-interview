# O(n)
def compress(s) :
    currentCharacterCount = 0
    compressed = ''

    for i, c in enumerate(s) :
        previousCharacter = s[i - 1]

        if i > 0 and c != previousCharacter :
            compressed += previousCharacter + str(currentCharacterCount)
            currentCharacterCount = 1
        else :
            currentCharacterCount += 1

        if i == len(s) - 1 :
            compressed += c + str(currentCharacterCount)

    if len(compressed) < len(s) : return compressed
    return s

assert(compress('aabbbbcddeeeeea') == 'a2b4c1d2e5a1')
assert(compress('aabbbbcddeeeeeaaaaaaaa') == 'a2b4c1d2e5a8')
assert(compress('aabbbbcddea') == 'aabbbbcddea')
print('Done')
