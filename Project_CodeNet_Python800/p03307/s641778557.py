n = int(input())

for i in range(1, 100000000, 1):
    if(n*i % 2==0):
        print(n*i)
        break