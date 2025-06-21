mod = 998244353

n=int(input())

t = list(map(int,input().split()))

tree = [0]*n

for i in t:
    tree[i] += 1

if tree[0] != 1 or t[0] != 0:
    ans = 0
else:
    ans = 1
    for i in range(1,n):
        ans = (ans*pow(tree[i-1],tree[i],mod))%mod
print(ans)
