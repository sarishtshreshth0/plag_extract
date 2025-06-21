N = int(input())
S = input()
res = 0

f = S[0]

for i in range(N):
  if S[i] != f:
    f = S[i]
    res += 1
    
print(res+1)