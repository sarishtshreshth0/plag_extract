a,b,c=map(int, input().split())
l=[a,b,c]
if c!=max(l) and c!=min(l):
	print('Yes')
else:
	print('No')