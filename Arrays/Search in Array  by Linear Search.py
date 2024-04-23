def sort(arr):
    for i in range(len(arr)):
         for j in range(len(arr)-i-1):
              if arr[j] > arr[j+1]:
                   temp = arr[j]
                   arr[j] = arr[j+1]
                   arr[j+1] = temp
def search(arr,number):
    for i in range(len(arr)):
        if number == arr[i]:
            return i;
            break
    return -1
arr =[]
try:
    array_index = int(input("Enter Array Indexes "))
    arr=[0]*array_index
except:
        print("Enter Integer!")
try:
    for i in range(len(arr)):
        arr[i] = int(input("Enter Number to insert in Array "))
except:
    print("Enter Number Please!")
number = int(input("Enter Number to search "))
check1 = search(arr,number)
if check1 != -1:
     print(f"{arr[check1]} found in index {check1}")
else:
     print(f"{arr[check1]} is not present in array")
sort(arr)
check2 = search(arr,number)
if check2 != -1:
     print(f"{arr[check1]} found in sorted array at index {check1}")
else:
     print(f"{arr[check2]} is not present in array")

print(f"Sorted Array\n{arr}")