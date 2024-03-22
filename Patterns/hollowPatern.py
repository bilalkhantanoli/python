def hollowPattern(row,column):
  for i in range(1,row+1):
    for j in range(1,column+1):
      if (i == 1 or i == row or j == 1 or j == column): #define Boundaries
        print('*',end='')
      else:
        print(' ',end='')
    print()
    
hollowPattern(4,5)