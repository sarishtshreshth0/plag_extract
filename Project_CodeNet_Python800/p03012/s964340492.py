n = int(input())
s = list(map(int, input().split()))

res = 10**9
for i in range(1,n):
    a = sum(s[:i])
    b = sum(s[i:])
    res = min(res, abs(a-b))
print(res)
