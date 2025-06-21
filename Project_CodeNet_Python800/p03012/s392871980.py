n = int(input())
w = list(map(int, input().split()))
x = 10000
for i in range(n+1):
    num = 0
    for j in range(i):
        num += w[j]
    x = min(x, abs((sum(w) - num) - num))
print(x)