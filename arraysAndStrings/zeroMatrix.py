def zeroMatrix(m) :
    zRows = set()
    zCols = set()

    for i, a in enumerate(m) :
        for j, num in enumerate(a) :
            if (m[i][j] == 0) :
                zRows.add(i)
                zCols.add(j)

    for r in range(0, len(zRows)) :
        a = m[r]

        for c in range(0, len(a)) :
            a[c] = 0
            
    for c in zCols :
        for r in range(0, len(m)) :
            m[r][c] = 0

m = [[1, 2, 0, 4, 5],
     [6, 0, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25],
     [26, 27, 28, 29, 30]]

def printRows(m) :
    for a in m : print(a)

printRows(m)
zeroMatrix(m)
print('====================================')
printRows(m)
