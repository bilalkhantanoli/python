def numberPattern(n):
  for i in range(1,n+1):
    for j in range(1,(n-i)+1):
      print(' ',end='')
    for j in range(1,i+1):
      print(i,end=' ')
    print()

numberPattern(5)


'''
    1 
   2 2    
  3 3 3   
 4 4 4 4  
5 5 5 5 5 
'''