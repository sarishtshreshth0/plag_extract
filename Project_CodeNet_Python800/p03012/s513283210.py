N = int(input())
W = list(map(int, input().split()))
 
S1 = 0
S2 = 0
ans = []
 
for i in range(N-1):
  S1 = sum(W[:i+1])
  S2 = sum(W[i+1:])
  ans.append(abs(S1-S2))
print(min(ans))