def pattern(n):
  for i in range(1,n+1):
    #print spaces
    for j in range(1,(n-i)+1):
      print(' ',end='')
    #print star
    for j in range(1,n+1):
      print('*',end='')
    print()

pattern(7)

'''
      *******
     *******
    *******
   *******
  *******
 *******
*******
'''