import sys
def largestNumber(numbers):
    largest = -sys.maxsize          #built in to find the lowest negative number
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

def smallestNumber(numbers):
    smallest = sys.maxsize          #built in to find the largest positive number
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest

numbers = [1,2,3,4,5,76,5,3,2,2111,23,43]
print(f"Largest number in array {largestNumber(numbers)}")
print(f"Smallest number in array {smallestNumber(numbers)}")

#time complixity O(n)