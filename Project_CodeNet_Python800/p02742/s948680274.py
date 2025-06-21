H,M=map(int,input().split())
if H==1:
	print("1")
elif M==1:
	print("1")
else:
	if H*M%2==0:
		print(H*M//2)
	else:
 		print((H*M)//2+1)
