n,a,b=map(int,input().split())
s=input()
c=0
c_b=0
for i in range(n):
    
    p=s[i]
    if p=='c':
        print('No')
    elif p=='a':
        if c<a+b:
            c+=1
            print('Yes')
        else:
            print('No')
    else:
        if c<a+b and c_b<b:
            c+=1
            c_b+=1
            print('Yes')
        else:
            print('No')
