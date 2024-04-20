def countingSort(array):
    largest = max(array)
    count = [0]*(largest +1)
    for i in range(len(array)):
        count[array[i]] +=1
    j=0
    for i in range(len(count)):
        while count[i] > 0:
            array[j] = i
            j+=1
            count[i]-=1

def descending(array):
    largest = max(array)
    count = [0] * (largest + 1)
    for num in array:
        count[num] += 1
    j = 0
    for i in range(len(count) - 1, -1, -1):
        while count[i] > 0:
            array[j] = i
            j += 1
            count[i] -= 1

array = [3, 6, 2, 1, 8, 7, 4, 5, 3, 1]
descending(array)
print(array)  


list = [5,4,1,3,2]
countingSort(list)
print(list)