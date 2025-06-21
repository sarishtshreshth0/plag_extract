n=int(input())
a=[list(map(int,input().split())) for _ in range(n-1)]

def arrive(time,now):
  if time>a[now][1]:
    time=(time+a[now][2]-1)//a[now][2]*a[now][2]+a[now][0]
  else: time=a[now][1]+a[now][0]
  if now==n-2:
    return time
  else:
    return arrive(time,now+1)

for i in range(n-1):
  print(arrive(a[i][1],i))
print(0)