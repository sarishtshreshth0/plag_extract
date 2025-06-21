M,D=map(int,input().split())
ans=0
for d in range(2,D+1):
	(a,b)=divmod(d,10)
	if b<2 or a<2:
		continue
	elif a*b <=M:
		ans+=1
print(ans)
	
	


