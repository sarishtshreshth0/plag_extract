n,a,b=map(int,input().split())
s=list(input())
nover=0
tot=0
for i in range(n):
    if tot<a+b:
        if s[i]=='a':
            print('Yes')
            tot+=1
        elif s[i]=='b' and nover<b:
            print('Yes')
            nover+=1
            tot+=1
        else:
            print('No')
    else:
        print('No')
