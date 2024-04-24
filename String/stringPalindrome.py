def palindrome(string):
    # left = 0
    # right = len(string) - 1
    # while left < right:
    #     if string[left] != string[right]:
    #         return False
    #     left +=1
    #     right -=1
    # return True

    for i in range(len(string) //2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

string = input('Enter string to check Palindrome ')
if palindrome(string):
    print(f"{string} is Palindrome")
else:
    print(f"{string} is not palindrome")

# palindrome = string[::-1]
# if string == palindrome:
#     print('String is Palindrome')
# else:
#     print('String is not palindrome')

    