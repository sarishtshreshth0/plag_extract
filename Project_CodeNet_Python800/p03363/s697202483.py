N = int(input())
A = list(map(int, input().split()))
L = [0]*(N+1)
for i in range(N):
  L[i+1]=L[i]+A[i]
result = 0
L_s = set(L)
D = {l:0 for l in L_s}
for l in L:
  D[l] += 1
for v in D.values():
  result += v*(v-1)//2
print(result)  