# string compression 
def stringCompression(s):
    newStr = ''
    i = 0
    while i < len(s):
        count = 1
        while i < len(s) - 1 and s[i] == s[i+1]:
            count +=1
            i +=1
        newStr += s[i]
        if count > 1:
            newStr += str(count)
        i+=1
    return newStr
# s = 'aaabbbccd'
s = 'abcd'
print(stringCompression(s))