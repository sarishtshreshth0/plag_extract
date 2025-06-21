n = int(input())
l = list(map(int, input().split()))
edge = [0 for x in range(n)]

if l[0] != 0:
    print(0)
    exit()

for i in l:
    edge[i]+=1

ans = 1
for i in range(1, n):
    ans *= edge[l[i] - 1]
    ans %= 998244353
print(ans)
