N,A,B=map(int,input().split())
S=' '+input()
AB=A+B
j=1
num=0
for i in range(1,N+1):
    if S[i]=='b' and num<AB and j<=B:
        print('Yes')
        j+=1
        num+=1
    elif S[i]=='a' and num<AB:
        print('Yes')
        num+=1
    else:
        print('No')
