import sys
def maxSubarrayKadane(n):
    maxSum = -sys.maxsize
    currentSum = 0
    for i in range(len(n)):
        currentSum = currentSum + n[i]
        if currentSum < 0:
            currentSum = 0
        if maxSum < currentSum:
            maxSum = currentSum
    return maxSum

n = [-2,-3,4,-1,-2,1,5,-3]
print(f"Max Sum : {maxSubarrayKadane(n)}")