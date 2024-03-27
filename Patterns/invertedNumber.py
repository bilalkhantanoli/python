# def invertedNumber(n):
#   k = n
#   for i in range(n+1,1,-1):
#     for j in range(1,k+1):
#       print(j,end='')
#     k-=1
#     print()
def invertedNumber(n):
  for i in range(1,n+1):
    for j in range(1,n-i+2):
      print(j,end='')
    print()
invertedNumber(5)


'''
12345
1234
123
12
1
'''