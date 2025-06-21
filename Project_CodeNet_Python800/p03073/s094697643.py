s = list(input())
n = len(s)
S = list(int(s[i]) for i in range(n))
if n %2 == 0:
  A = [0,1] * (n//2)
  B = [1,0] * (n//2)
else:
  A = [0,1] * (n//2) + [0]
  B = [1,0] * (n//2) + [1]

ansA = 0
ansB = 0
for i in range(n):
  ansA += abs(S[i]-A[i])
  ansB += abs(S[i]-B[i])
  
print(min(ansA,ansB))