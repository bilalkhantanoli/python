import sys
def search(matrix,key):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == key:
                print(f"Number found at index ({i} , {j})")
                return True
    print("Number not Found")
    return False

def largestAndSmallest(matrix):
    largest = -sys.maxsize
    smallest = sys.maxsize
    largest_i = largest_j = smallest_i = smallest_j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                largest_i, largest_j = i, j
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]
                smallest_i, smallest_j = i, j
    print(f"Largest Number {largest} at index ({largest_i}, {largest_j})")
    print(f"Smallest Number {smallest} at index ({smallest_i}, {smallest_j})")



rows , col = 3,3
matrix = []
for i in range(rows):
    row = []
    for j in range(col):
        row.append(int(input('Enter Number ')))
    matrix.append(row)
print("matrix")
for row in matrix:
    print(row)

search(matrix,6)
largestAndSmallest(matrix)