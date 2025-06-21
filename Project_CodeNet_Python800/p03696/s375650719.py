n=int(input())
s=list(input())
over=0
left=0
right=0
center=""
for i in s:
    if over==0 and i==")":
        left+=1
    elif over!=0 and i==")":
        over-=1
    else:
        over+=1
    center+=i
right=over
print("("*left+center+")"*right)