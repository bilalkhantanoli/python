number = [11,2,3,4,5,6,7,8,9]

first_pointer = 0
last_pointer = len(number) - 1

while first_pointer < last_pointer:
    temp = number[first_pointer]
    number[first_pointer] = number[last_pointer]
    number[last_pointer] = temp
    first_pointer +=1
    last_pointer -=1

print(number)