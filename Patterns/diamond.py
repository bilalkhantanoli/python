def diamond_pattern(n):
  for i in range(1,n+1):
    for j in range(1,(n-i)+1):
      print(' ',end='')
    for j in range(1,2*(i-1)+1+1):#2(i)-1
      print('*',end='')
    print()
  for i in range(n,0,-1):
    for j in range(1,(n-i)+1):
      print(' ',end='')
    for j in range(1,2*(i-1)+1+1):
      print('*',end='')
    print()

diamond_pattern(4)


'''
   *
  ***
 *****
*******
*******
 *****
  ***
   *
'''