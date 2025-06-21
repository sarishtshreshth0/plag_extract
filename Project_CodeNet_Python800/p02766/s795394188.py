n,k = map(int,input().split())
for i in range(n):
    n = n // k
    if n == 0:
        print(i + 1)
        exit()