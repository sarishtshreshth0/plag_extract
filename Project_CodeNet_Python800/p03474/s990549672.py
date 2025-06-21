A,B=map(int,input().split())
S=list(input())
a=[]
for i in range(len(S)):
    if 0<=i and i<=A-1:
        if S[i].isdecimal()==True:
            a.append('Yes')
        else:
            a.append('No')
    elif i==A:
        if S[i]=='-':
            a.append('Yes')
        else:
            a.append('No')
    elif i>A: 
        if S[i].isdecimal()==True:
            a.append('Yes')
        else:
            a.append('No')
if 'No' in a:
    print('No')
else:
    print('Yes')