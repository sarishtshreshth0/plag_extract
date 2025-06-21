n = int(input())
w = list(map(int, input().split()))
s = sum(w)
counter = 0
ans = 1000000
for i in range(n):
    counter += w[i]
    rest = s - counter
    diff = abs(counter - rest)
    ans = min(ans, diff)
print(ans)