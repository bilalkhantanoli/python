def selectionSort(array):
    for turn in range(len(array)-1):
        minPosition = turn
        for j in range(turn+1,len(array)):
            if array[minPosition] > array[j]: #change the sign to less for decreasing order
                minPosition = j
        
        temp = array[minPosition]
        array[minPosition] = array[turn]
        array[turn] = temp
#Time Complexity O(n2)

def descending(array):
    for turn in range(len(array)-1):
        pos = turn
        for j in range(turn+1,len(array)):
            if array[pos] < array[j]:
                pos = j
        temp = array[pos]
        array[pos] = array[turn]
        array[turn] = temp


array = [3,6,2,1,8,7,4,5,3,1]
descending(array)
print(array)    

list = [5,4,1,2,3]
selectionSort(list)
print(list)