n=int(input())
red=[]
blue=[]
for i in range(n):
  a,b=map(int,input().split())
  red.append([a,b])
for j in range(n):
  a,b=map(int,input().split())
  blue.append([a,b])
blue.sort(key=lambda x:x[0])
red.sort(key=lambda x:x[1],reverse=True)

cnt=0
for x,y in blue:
  for i in range(n):
    if red[i][0]<x and red[i][1]<y:
      cnt+=1
      red[i][0]=float("INF")
      red[i][1]=float("INF")
      break
print(cnt)   
      
  
