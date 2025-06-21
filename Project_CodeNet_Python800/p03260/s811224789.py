#abc109 a
a,b=map(int,input().split())
flag=False
for c in range(1,4):
    x=a*b*c
    if x%2==1:
        flag=True
        break
if flag:
 	print("Yes")
else:
 	print("No")