N,A,B=map(int,input().split())
S=input()

cnt=0
fl=0

for i in range(N):
    if S[i]=='a' and cnt<A+B:
        print('Yes')
        cnt+=1
    elif S[i]=='b' and cnt<A+B and fl<B:
        print('Yes')
        cnt+=1
        fl+=1
    else:
        print('No')