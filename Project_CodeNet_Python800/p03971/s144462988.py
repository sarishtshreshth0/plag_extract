N,A,B=map(int,input().split())
S=input()

P=0
Q=1
for i in range(len(S)):
    if S[i]=='a'and P<A+B:
        print('Yes')
        P+=1
    elif S[i]=='b'and P<A+B and Q<=B:
        print('Yes')
        P+=1
        Q+=1
    elif S[i]=='c ':
        print('No')
    else:
        print('No')