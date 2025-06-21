mn=1145141919
n=int(input())
li=list(map(int,input().split()))

for i in range(n):
  res=abs(sum(li[:i])-sum(li[i:]))
  if res<mn:
    mn=res
print(mn)
