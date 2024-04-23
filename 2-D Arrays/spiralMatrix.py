def spiralMatrix(matrix):
    startRow = 0
    startCol = 0
    endRow = len(matrix) - 1
    endCol = len(matrix[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        #top boundary
        for j in range(startCol,endCol+1):
            print(matrix[startRow][j],end=" ")

        #right boundary
        for i in range(startRow+1,endRow+1):
            print(matrix[i][endCol],end=" ")
        
        #bottom boundary
        for j in range(endCol-1,startCol-1,-1):
            if startRow == endRow:
                break
            print(matrix[endRow][j],end=" ")

        # left boundary
        for i in range(endRow-1,startRow,-1):
            if startCol == endCol:
                break
            print(matrix[i][startCol],end=" ")
        startRow +=1
        startCol +=1
        endRow -=1
        endCol-=1

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]
          ]
spiralMatrix(matrix)

# print(matrix)