#for binary search the array must be sorted we just implement binary search here

def binarySearch(numbers,key):
    start = 0 
    end = len(numbers)-1
    while start <= end: #condition
        mid = (start + end)//2 #find mid of the array and // is used to get in integer value
        if numbers[mid] == key:
            return mid
        elif numbers[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


numbers = [2,4,6,8,10,12,14]
print(f"Index # {binarySearch(numbers,10)}")

#time coplexity -> O(log n)