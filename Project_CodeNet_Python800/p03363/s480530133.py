import collections

n=int(input())
arr=[0]+list(map(int,input().split()))
for i in range(n):
  arr[i+1]+=arr[i]
cnt=collections.Counter(arr)
ans=0
for val in cnt.values():
  ans+=val*(val-1)//2
print(ans)