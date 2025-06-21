from collections import Counter

n=int(input())
a=list(map(int,input().split()))

min_v=min(a)
max_v=max(a)

c=Counter(a)

ans=0
for i in range(min_v,max_v+1):
  t_ans=c[i-1]+c[i]+c[i+1]
  ans=max(ans,t_ans)

print(ans)