# Rotates a square matrix 90 degrees clockwise.  O(N^2) where N is the size of the matrix.
def rotate(m):
    n = len(m)

    for i, r in enumerate(m):
        for j, c in enumerate(r, start=i):
            if j >= n - i - 1:
                break

            # Right
            sidelined = m[j][n - i - 1]
            m[j][n - i - 1] = m[i][j]

            # Bottom
            temp = m[n - i - 1][n - j - 1]
            m[n - i - 1][n - j - 1] = sidelined
            sidelined = temp

            # Left
            temp = m[n - j - 1][i]
            m[n - j - 1][i] = sidelined
            sidelined = temp

            # Original
            m[i][j] = sidelined


m = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]

expected = [
    ['M', 'I', 'E', 'A'],
    ['N', 'J', 'F', 'B'],
    ['O', 'K', 'G', 'C'],
    ['P', 'L', 'H', 'D']
]

rotate(m)
print(m)

assert m == expected

m = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y']
]

expected = [
    ['U', 'P', 'K', 'F', 'A'],
    ['V', 'Q', 'L', 'G', 'B'],
    ['W', 'R', 'M', 'H', 'C'],
    ['X', 'S', 'N', 'I', 'D'],
    ['Y', 'T', 'O', 'J', 'E']
]

rotate(m)
print(m)

assert m == expected

print('Passed!')
