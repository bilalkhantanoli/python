def characterPattern(n):
    ch = 'A' #initalize character
    for i in range(1,n+1):          #outer loop
        for j in range(1,i+1):      #inner loop
            print(ch,end='')        #print character
            ch = chr(ord(ch)+1)     #built-in function ord()-> convert character into unicode  and chr() -> convert unicode to character
        print()

characterPattern(6) #func calling

#ouput
'''
A
BC
DEF
GHIJ
KLMNO
PQRSTU
'''