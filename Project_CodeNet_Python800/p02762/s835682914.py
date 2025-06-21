
# count the size of the component to which a node belongs to 
# subtract all the direct friendship and direct blockships
# subtract 1 itself
import sys
import os
sys.setrecursionlimit(1000000)
from collections import defaultdict
adj = defaultdict(list)
adj1=defaultdict(list)
szc = [ 0 for i in range(300000)]
which =[0 for i in range(300000)]
vis = [0 for i in range(300000)]
tot =0
def dfs1(u):
	global tot
	vis[u]=1
	which[u]=tot
	szc[tot]=szc[tot]+1
	for i in adj[u]:
		if vis[i]==1:
			continue
		dfs1(i)
def main():
	global tot
	n , m , k = map(int, input().split())
	bk =[0 for i in range(n+1)]
	fd =[0 for i in range(n+1)]
	for i in range(m):
		x, y = map(int ,input().split())
		adj[x].append(y)
		adj[y].append(x)
		fd[x]=fd[x]+1
		fd[y]=fd[y]+1
	for i in range(k):
		x, y = map(int , input().split())
		adj1[x].append(y)
		adj1[y].append(x)
	for i in range(1, n+1):
		if vis[i]!=1:
			tot = tot+1
			dfs1(i)
	ans=[]
	for i in range(1, n+1):
		res = szc[which[i]]
		res = res-fd[i]
		res = res-1
		for j in adj1[i]:
			if which[j]==which[i]:
				res =res -1
		ans.append(res)
	print(*ans)
		
if __name__=="__main__":
	main()