def hollow(n):
  for i in range(1,n+1):
    #print spaces
    for j in range(1,(n-i)+1):
      print(' ',end='')
    #print star
    for j in range(1,n+1):
      if (j==1 or j == n or i == 1 or i == n):
        print('*',end='')
      else:
        print(' ',end='')
    print()

hollow(5)

'''
    *****
   *   *
  *   *
 *   *
*****
'''