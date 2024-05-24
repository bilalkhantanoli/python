#get ith bit 
#n & (1<<i)
def getIthBit(n, i):
    bitmask = 1 << i
    if n & bitmask == 0:
        return 0
    else:
        return 1

print(getIthBit(10,2))

#set ith bit
# n | 1<<i
def setIthBit(n, i):
    bitmask = 1 << i
    return bitmask | n 

print(setIthBit(10,2))

#clear ith bit
# n ~(i<<i)
def clearIthBit(n, i):
    bitmask = ~(1 << i)
    return n & bitmask

print(clearIthBit(10,1))
