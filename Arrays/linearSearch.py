def linearSearch(array,key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

# array = [2,3,4,6,7,8,10,12,14]
# key = 10
array = ['hello','this','is','an','array']
key = 'hi'

result = linearSearch(array,key)
if result == -1:
    print("Not Found")
else:
    print(f"Found at Index Number {result}")
#time Complexity O(n)

