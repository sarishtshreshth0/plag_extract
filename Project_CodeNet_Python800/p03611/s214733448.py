from math import*
from bisect import*
import copy

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
brr=copy.deepcopy(arr)
brr=list(set(brr))
brr.sort()
#print(arr)
#print(brr)
ans=0
#print(bisect_right(arr,6))
for i in range(len(brr)):
	d=bisect_left(arr,brr[i])
	c=bisect_right(arr,brr[i]+2)
#	print(d,c)
	if ans<c-d:
		ans=c-d
print(ans)