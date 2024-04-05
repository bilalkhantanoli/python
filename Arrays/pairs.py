n = [2,4,6,8,10]
for i in range(len(n)+1):
    for j in range(i+1,len(n)):
        print(f"({n[i]},{n[j]})",end=' ')
    print()