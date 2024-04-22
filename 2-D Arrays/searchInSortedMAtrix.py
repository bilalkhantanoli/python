def stairCase(matrix,key):
#top right approach
    '''
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == key:
            print(f"Found at Index ({row},{col})")
            return
        elif key < matrix[row][col]:
            col -=1
        else:
            row +=1
    print("Key Not found")
    '''
#bottom left approach
    col = 0
    row = len(matrix) -1
    while col < len(matrix) and row >=0:
        if matrix[row][col] == key:
            print(f"Found at Index ({row},{col})")
            return
        elif key < matrix[row][col]:
            row -=1
        else:
            col +=1
    print("Key not found")

matrix = [
    [10,20,30,40],
    [15,25,35,45],
    [27,19,37,48],
    [32,33,39,50]
]
key = 50
stairCase(matrix,key)