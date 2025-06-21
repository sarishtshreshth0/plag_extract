n=int(input())
 
if n!=0:
	ans1=n//500
	sub=n-(ans1*500)
	ans2=sub//5
 
	print((ans1*1000)+(ans2*5))
 
else:
	print(0)