n=int(input())
s=input()
stack=0
needleft=0
needright=0
for c in s:
    if c=='(':
        needright+=1
    else:
        if needright>0:
            needright-=1
        else:
            needleft+=1
s='('*needleft+s
s+=')'*needright
print(s)