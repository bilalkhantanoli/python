def invertedStarPattern(n):
    for i in range(1,n+1):
        for j in range(1,(n-i+1)+1):
            print('*',end='')
        print()

invertedStarPattern(4)
'''
****
***
**
*
'''