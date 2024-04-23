def main():
    list = [1,2,3,4,5,6,7,8,-1,0]
    print(list)
    n=6
    pos = int(input("Enter Position where you insert "))
    num = int(input("Enter Number "))
    print("Before Insertion\n")
    for i in range(0,n-1):
        print(list[i],end=" ")
    insert(list,pos-1,num,n)
    n+=1
    print("\nAfter Insertion")
    for i in range(0, n):
        print(list[i],end=" ")

def insert(list, pos, num, n):
    for i in range(n - 1, pos - 1, -1):
        list[i + 1] = list[i]
    list[pos] = num
if __name__ == "__main__":
    main()