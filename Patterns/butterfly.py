def butterfly(n):
  # 1 half
  for i in range(1,n+1):
    #stars
    for j in range(1,i+1):
      print('*',end='')
    #spaces 2(n-i)
    for j in range(1,2*(n-i) +1):
      print(" ",end='')
    #stars
    for j in range(1,i+1):
      print('*',end='')
    print()
  # second half
  for i in range(n,0,-1):
    #stars
    for j in range(1,i+1):
      print('*',end='')
    #spaces 2(n-i)
    for j in range(1,2*(n-i) +1):
      print(" ",end='')
    #stars
    for j in range(1,i+1):
      print('*',end='')
    print()

butterfly(5)


'''
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *
'''
