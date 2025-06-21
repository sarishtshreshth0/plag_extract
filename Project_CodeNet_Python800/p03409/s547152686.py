N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
B=[list(map(int,input().split())) for i in range(N)]
B.sort(key=lambda x:x[0])
A.sort(key=lambda x:x[1])
C=[0]*N
cnt=0
for i in range(N):
  for j in range(N):
    if C[j]==0 and A[-i-1][0]<B[j][0] and A[-i-1][1]<B[j][1]:
      C[j]=1
      cnt+=1
      break
print(cnt)