N,A,B=map(int,input().split())
S=list(input())
yesno=[]
a=0
b=0
c=1
for i in range(N):
    if S[i]=='a':
        if a+b<A+B:
            yesno.append('Yes')
            a+=1
        else:
            yesno.append('No')
    elif S[i]=='b':
        if a+b<A+B and c<=B:
            yesno.append('Yes')
            b+=1
            c+=1
        else:
            yesno.append('No')
    else:
        yesno.append('No')
for i in range(N):
    print(yesno[i])