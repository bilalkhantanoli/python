def insertionSort(array):
    for i in range(1,len(array)):
        current = array[i]
        previous = i-1
        while (previous >=0) and (array[previous] > current): # for decreasing order change the greater sign to less than
            array[previous+1] = array[previous]
            previous -=1
        array[previous+1] = current

#Time Complexity O(n2)
def descending(array):
    for i in range(1,len(array)):
        current = array[i]
        prev = i-1
        while prev >= 0 and array[prev] < current:
            array[prev+1] = array[prev]
            prev-=1
            array[prev+1] = current




array = [3,6,2,1,8,7,4,5,3,1]
descending(array)
print(array)

list = [5,4,1,3,2]
insertionSort(list)
print(list)