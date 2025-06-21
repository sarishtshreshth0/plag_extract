n = int(input())
w = list(map(int, input().split()))
ret = float('inf')
for i in range(n):
    x = sum(w[:i+1])
    y = sum(w[i+1:])
    ret = min(ret, abs(x-y))
print(ret)