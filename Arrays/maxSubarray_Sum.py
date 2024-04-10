import sys

def maxSubarraySum(n):
    maxSum = -sys.maxsize
    for i in range(len(n)+1):
        start = i
        for j in range(i+1,len(n)):
            end = j
            sum = 0
            for k in range(start, end+1):
                sum = n[k] + sum
            print(sum)
            if(maxSum < sum):
                maxSum = sum
    print(f"Max Sum of Subarray is {maxSum}")
def maxSubarraySum_prefix(n):
    maxSum = -sys.maxsize
    prefix_array=[]
    prefix_array.append(n[0])
    for i in range(1,len(n)):
        prefix_array.append(prefix_array[i-1] + n[i])
    for i in range(len(n)+1):
        start = i
        for j in range(i+1,len(n)):
            end = j
            sum =  prefix_array[end] if start ==0 else prefix_array[end] - prefix_array[start-1]     # formula to calculate the sum of sub array
            if(maxSum < sum):
                maxSum = sum
    print(f"Max Sum of Subarray is {maxSum}")    


n = [1,-2,6,-1,3]
# maxSubarraySum(n) #TC O(n3)

maxSubarraySum_prefix(n) # TC O(n2)
