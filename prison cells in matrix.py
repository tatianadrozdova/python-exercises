"""
There is a matrix 8 x 8. If cell is dead (0) and there is 3rd neighbor of the cell (1), the cell is born.
If cell is alive and cell has 2nd and 3rd neighbor of the cell, the cell stays alive.

matrix
00011
00110
00110
00011
00011

result matrix
[0, 0, 1, 0, 0]
[0, 1, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 1, 0, 0]

list view of matrix:
matrix = [[0,0,0,1,1],[0,0,1,1,0], [0,0,1,1,0], [0,0,0,1,1], [0,0,0,1,1]]
result [[0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
"""

import copy

def matrixCells(matrix):
    newMatrix = copy.deepcopy(matrix)
    
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix)):
            
            if x == len(matrix) - 1:
                newMatrix[y][x] = 0
                print("1st:x = %s, y = %s" % (x, y))

            elif matrix[y][x] == 0:
                if matrix[y][x + 1] == 1:
                    newMatrix[y][x] = 1
                    print("2nd yes:x = %s, y = %s" % (x, y))
               
                    
            elif matrix[y][x] == 1:
                if y == 0:
                    newMatrix[y][x] = 0
                    print("3rd 1st yes:x = %s, y = %s" % (x, y))
                
                elif matrix[y][x + 1] == 1 and matrix[y - 1][x + 1] == 1:
                    print("3rd  2nd yes y == 0:x = %s, y = %s" % (x, y))
                    newMatrix[y][x] = 1                    
                else:
                    newMatrix[y][x] = 0
                    print("3rd no:x = %s, y = %s" % (x, y))
                
    for k in matrix:
        print (k)
    print("")

    for n in newMatrix:
        print (n)
    return newMatrix
    
matrix = [[0,0,0,1,1],[0,0,1,1,0], [0,0,1,1,0], [0,0,0,1,1], [0,0,0,1,1]]                         
print(matrixCells(matrix))

