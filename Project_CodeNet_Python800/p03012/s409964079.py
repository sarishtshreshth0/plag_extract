N=int(input())
S=list(map(int, input().split()))
A=[]
for i in range(1,N):
  A.append(abs(sum(S[:i])-sum(S[i:])))
print(min(A) if not A==[] else abs(S[0]-S[1]))