def diagonalSum(matrix):
    sum = 0
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if i == j:
    #             sum += matrix[i][j]
    #             # print(matrix[i][j])
    #         elif i+j == len(matrix) -1:
    #             # print(matrix[i][j])
    #             sum += matrix[i][j]

    for i in range(len(matrix)):
        # pd
        sum += matrix[i][i]

        # sd
        if i != len(matrix) - i -1:
            sum += matrix[i][len(matrix) - i -1]

    return sum
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]
          ]
print(diagonalSum(matrix))