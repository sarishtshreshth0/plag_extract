n = int(input())
d = list(map(int, input().split()))

l = [0]*(max(d)+1)
for i in d:
    l[i] += 1

if d[0] != 0 or l[0] != 1:
    print(0)
    exit()

ans = 1
for i in range(1, len(l)):
    ans *= l[i-1]**l[i]

print(ans%998244353)