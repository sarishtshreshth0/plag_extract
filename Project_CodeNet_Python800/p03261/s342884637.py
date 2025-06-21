n=int(input())
w=[input()for i in range(n)]
isSaid=[]
safe=True
for i in w:
    if i in isSaid or (len(isSaid)>0 and isSaid[-1][-1]!=i[0]):
        safe=False
    else:
        isSaid.append(i)
if safe:
    print("Yes")
else:
    print("No")