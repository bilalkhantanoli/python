'''
1. minimum of bars > 2
2. bars in proper asc/dsc not trapped water

(water level - bar level ) * width = trapped water

water level => min(maxLeft Boundary , maxRight Boundary)

trappedWater = waterLevel - Height 

to calculate max boundary we used auxiliary array's / helper arrays
create two arrays to store left and right maximum values
'''

def trappedRainwater(height):
    #calculate the left max boundary
    leftMax = [0] * len(height)
    leftMax[0] = height[0]
    for i in range(1,len(height)):
        leftMax[i] = max(height[i],leftMax[i-1]) #assign max in left max array

    # print(leftMax)
    #right max boundary
    rightMax = [0] * len(height)
    rightMax[len(height) - 1 ] = height[len(height)-1]
    for i in range(len(height)-2,-1,-1):
        rightMax[i] = max(height[i], rightMax[i+1])
    # print(rightMax)

    trappedWater = 0
    for i in range(len(height)):
        #water level = min(leftmax , rightmax)
        waterLevel = min(leftMax[i], rightMax[i])
        #trapped water = waterlevel - height
        trappedWater += waterLevel - height[i]
    
    return trappedWater
list = [4,2,0,6,3,2,5]
print(trappedRainwater(list))