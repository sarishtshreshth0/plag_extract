from collections import Counter

N=int(input())
A=list(map(int,input().split()))
B=[A[0]]
for i in range(1,N):
  B.append(B[-1]+A[i])
B = [0]+B
ans=0

d=dict(Counter(B))
for num in d:
  ans += d[num]*(d[num]-1)//2
  
print(ans)