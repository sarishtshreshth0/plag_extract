N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

nodes = [0] * N

for d in D:
  nodes[d] += 1

ans = 0
if nodes[0]==1 and D[0]==0:
  pre_n = 1
  ans = 1
  for n in nodes:
    ans = (ans * pre_n**n) % MOD
    pre_n = n

print(ans)