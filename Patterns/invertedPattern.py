def invertedPattern(row):
  for i in range(1,row+1):
    for j in range(1,row-i+1):
      print(' ',end='')
    for j in range(1,i+1):
      print('*',end='')
    print()

invertedPattern(4)