# bit manipulation
# and operator
print(5 & 6)

#| or operator
print(5 | 6)

# ^ XOR operator
print(5^6)

# ~ one compliment
#one's compliment again of compliment and add 1 bit to extract digit
print(~5)

# binary left shift 
# a<<b = a * 2^b
print(5<<2)

# binary right shift
#formula a>>b = a//2^b
print(6>>1)


#question 1 check if a number is even or odd
# solution -> for odd value the lsb(least significance bit) is 1 and for even the lsb is 0
def oddOrEven(n):
    bitmask = 1
    if n & bitmask == 0:
        print('Even Number')
    else:
        print('Odd Number')

oddOrEven(11)
oddOrEven(5)
oddOrEven(6)