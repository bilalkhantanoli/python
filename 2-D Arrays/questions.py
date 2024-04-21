def question1(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 7:
                count +=1
    return count

def question2(matrix):
    sum = 0
    for i in range(len(matrix[0])):
        sum += matrix[1][i]
    return sum

def transpose(matrix):
    transpose = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for i in range(len(transpose)):
        for j in range(len(transpose[0])):
            transpose[i][j] = matrix[j][i]
    print(transpose)

matrix3 = [
    ['a11','a12','a13'],
    ['a21','a22','a23']
]
transpose(matrix3)

matrix = [
    [4,7,8],
    [8,8,7]
]
print(question1(matrix))

matrix1 = [
    [1,4,9],
    [11,4,3],
    [2,2,3]
]
print(question2(matrix1))

