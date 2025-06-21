import collections
n = int(input())
a = list(map(int,input().split()))
lst = collections.defaultdict(int)
for i in a:
  lst[i] += 1
  lst[i-1] += 1
  lst[i+1] += 1
  
lst = sorted(lst.items(),reverse=True,key=lambda x:x[1])
print(lst[0][1])