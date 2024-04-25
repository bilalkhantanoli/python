#shortest path
# shortest path = ((x2-x1)^2+(y2-y1)^2)1/2
from math import sqrt
def shortestPath(path):
    path = path.lower()
    x = 0
    y = 0 
    for i in range(len(path)):
        if path[i] == 'n':
            y += 1
        elif path[i] == 's':
            y -= 1
        elif path[i] == 'w':
            x -= 1
        elif path[i] == 'e':
            x += 1
        else: 
            return
    x2 = x*x
    y2 = y*y
    return sqrt(x2 + y2)
path = 'WNEENESENNN'
print(f"Sortest path is {shortestPath(path)}")

#substring
def substring(str,si,ei):
    substring = ''
    for i in range(si,ei):
        substring += str[i]
    return substring

str = 'helloWOrld'
# print(substring(str,0,5))


#return largest string in lexicographic order
def largestString():
    strings = ['apple', 'mango', 'bannana']
    largest = strings[0]
    for i in range(len(strings)):
        if largest < strings[i]:
            largest = strings[i]
    print(largest)

largestString()

# convert each first letter of word to upper case letter

def firstLetter(s):
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i].capitalize()

    return ' '.join(s)

s = 'hi, i am bilal'
print(firstLetter(s))