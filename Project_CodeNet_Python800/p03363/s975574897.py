N = int(input())
S = list(map(int, input().split()))

d = {0:1}
temp = 0

for i in range(N):
    temp += S[i]
    if temp in d:
        d[temp] += 1
    else:
        d.setdefault(temp, 1)

ans = 0
for num in d.values():
    ans += num*(num-1)//2

print(ans)
