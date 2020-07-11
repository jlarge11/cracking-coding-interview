# Goes through an M x N matrix.  For every element with value 0, it will mark every element in that row and column with 0.
# O(M x N)
def zero(m):
    zero_rows = []
    zero_columns = []

    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c == 0:
                zero_rows.append(i)
                zero_columns.append(j)

    for i in zero_rows:
        for j, c in enumerate(m[i]):
            m[i][j] = 0

    for j in zero_columns:
        for i, r in enumerate(m):
            m[i][j] = 0


m = [
    [0, 1, 5, 8, 5],
    [1, 4, 0, 3, 2],
    [6, 7, 2, 8, 3]
]

expected = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 7, 0, 8, 3]
]


zero(m)

for r in m:
    print(r)

assert m == expected

print('Passed!')
