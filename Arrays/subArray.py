n = [2,4,6,8,10]
ts = 0
for i in range(len(n)+1):
    start = i
    for j in range(i+1,len(n)):
        end = j
        for k in range(start,end+1):
            print(n[k],end=' ')
        print()
        ts+=1
    print()
print("Total subarray ",ts)