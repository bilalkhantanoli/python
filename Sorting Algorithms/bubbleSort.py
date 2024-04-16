def bubblesort(array):
    for turn in range(len(array)-1):
        for j in range(len(array)-1-turn):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
#Time Complexity O(n2)

def descending(array):
    for turn in range(len(array)-1):
        for j in range(len(array)-1-turn):
            if array[j] < array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp    


array = [3,6,2,1,8,7,4,5,3,1]
descending(array)
print(array)

list = [5,4,1,3,2]
bubblesort(list)
print(list)