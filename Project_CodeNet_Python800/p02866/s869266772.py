from collections import defaultdict
dic = defaultdict(int)
MOD = 998244353
N = int(input())
A = list(map(int,input().split()))
MAX = max(A)
store = [0 for _ in range(MAX+1)]

for x in A:
  store[x] += 1

if A[0] != 0 or store[0] != 1:
  print(0)
  exit()

ans = 1
for i in range(MAX):
  ans = ans*pow(store[i],store[i+1],MOD)
print(ans%MOD)