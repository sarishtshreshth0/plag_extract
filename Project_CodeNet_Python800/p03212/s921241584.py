from itertools import product
n=int(input())
tmp=2
ans=0
Flag=True
while Flag:
    tmp+=1
    iterator=product(range(3),repeat=tmp)
    for idxs in iterator:
        num=''.join(map(str,idxs))
        num753=str(num).replace('0', '3').replace('1', '5').replace('2', '7')
        if '7' in num753 and '5' in num753 and '3' in num753:
            if int(num753)<=n:
                ans+=1
            else:
                Flag=False
                break
print(ans)