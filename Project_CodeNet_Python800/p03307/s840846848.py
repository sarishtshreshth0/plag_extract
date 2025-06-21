n = int(input())
m = max(2, n)
for i in range(m, 2*n+1, m):
    if i % 2 == 0:
        print(i)
        exit(0)
