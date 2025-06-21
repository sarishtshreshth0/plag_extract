M,D = map(int,input().split())
count=0
for i in range (20,D+1):
	j=i//10
	k=i%10
	if j*k<=M and k>1:
		count+=1
print(count)