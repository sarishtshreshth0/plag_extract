N=int(input())
ab=[list(map(int,input().split())) for _ in range(N)]
cd=[list(map(int,input().split()))+[1] for _ in range(N)]

AB=sorted(ab, key=lambda x:x[1], reverse=True)
CD=sorted(cd, key=lambda x:x[0])
cnt=0

for i in range(N):
  for j in range(N):
    if AB[i][0]<CD[j][0] and AB[i][1]<CD[j][1] and CD[j][2] ==1:
      cnt+=1
      CD[j][2]-=1
      break
      
print(cnt)