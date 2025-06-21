N,A,B=map(int,input().split())
S=input()
total=0
foreign=0
ans=['' for i in range(len(S))]

for i in range(len(S)):
    if S[i]=='a':
        if total<A+B:
            total+=1
            ans[i]='Yes'
        else:
            ans[i]='No'
    elif S[i]=='b':
        if total<A+B and foreign<B:
            total+=1
            foreign+=1
            ans[i]='Yes'
        else:
            ans[i]='No'
    else:
        ans[i]='No'

for anss in ans:
    print(anss)