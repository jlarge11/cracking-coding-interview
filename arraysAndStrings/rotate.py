'''
a   b   c   d
e   f   g   h
i   j   k   l
m   n   o   p

m   i   e   a
n   j   f   b
o   k   g   c
p   l   h   d

1, 1 -> 1, 4
1, 2 -> 2, 4
1, 3 -> 3, 4
1, 4 -> 4, 4

Anything in row 0 goes to column 3
Anything in row 1 goes to column 2
Anything in row 2 goes to column 1
Anything in row 3 goes to column 0
Anything in row r goes to column n -1 - r

Anything in column 0 goes to row 0
Anything in column 1 goes to row 1
Anything in column 2 goes to row 2
Anything in column 3 goes to row 3
Anything in column c goes to row c

(0, 0), (0, 3), (3, 3), (3, 0)
(0, 1), (1, 3), (3, 2), (2, 0)
(0, 2), (2, 3), (3, 1), (1, 0)
(0, 3) skip

(1, 1), (1, 2), (2, 2), (2, 1)
(1, 2) skip

(r, c), (c, n - 1 - r), (n - 1 - r, n - 1 - c), (n - 1 - c, r)
'''
def replace(m, e, v) :
    replaced = m[e[0]][e[1]]
    m[e[0]][e[1]] = v
    return replaced

def rotate(m) :
    n = len(m)

    for r in range(0, n) :
        for c in range(r, n - 1 - r) :
            e1 = (r, c)
            e2 = (c, n - 1 - r)
            e3 = (n - 1 - r, n - 1 - c)
            e4 = (n - 1 - c, r)

            v = m[r][c]
            v = replace(m, e2, v)
            v = replace(m, e3, v)
            v = replace(m, e4, v)
            v = replace(m, e1, v)

m = [['a', 'b', 'c', 'd', 'e'],
     ['f', 'g', 'h', 'i', 'j'],
     ['k', 'l', 'm', 'n', 'o'],
     ['p', 'q', 'r', 's', 't'],
     ['u', 'v', 'w', 'x', 'y']]

def printRows(m) :
    for a in m : print(a)

printRows(m)
rotate(m)
print('====================')
printRows(m)
