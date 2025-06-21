from collections import deque

N=int(input())
a=[0]*(N-1)
b=[0]*(N-1)
c=[set() for _ in range(N)] # 使用している色
d=[set() for _ in range(N)] # 隣接リスト
e=[ False for _ in range(N)] #訪問ずみかどうか
f=[0]*N  #答え
for i in range(N-1):
    a[i],b[i] = map(int,input().split())
    d[a[i]-1].add(b[i]-1)
    d[b[i]-1].add(a[i]-1)

maxi=max([len(d[i]) for i in range(N-1)])
print(maxi)
#print("c:",c)
#print("d",d)
#print("e",e)

#x=0としてBFSする

v=deque([0])
e[0]=True
color=1

while v:
  p = v.popleft()
  for q in d[p]:
    if e[q]==False:
      while color in c[p]:
        color +=1
        if color>maxi:
          color=1
      c[p].add(color)
      c[q].add(color)
      f[q]=color
      e[q]=True
      v.append(q)
      
for i in range(N-1):
  print( f[b[i]-1])