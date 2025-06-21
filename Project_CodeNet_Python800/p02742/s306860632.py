H,W=map(int,input().split())
ans=0
if H==1 or W==1:
	ans=1
else:
	if H%2==0:
		ans=H*W//2
	else:
		if W%2!=0:
			ans = H*(W-1)//2+(H//2+1)
		else:
			ans=H*W//2
print(ans)