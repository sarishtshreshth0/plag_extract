from collections import Counter

N=int(input())
s=list(map(int,input().split()))

result=[0]
for i in s:
	result.append(result[-1]+i)

a=Counter(result)
ans=0
for j in a.values():
	ans+=j*(j-1)//2

print(ans)