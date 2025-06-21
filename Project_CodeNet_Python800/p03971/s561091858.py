
N,A,B = map(int,input().split())
S = input()
total = A+B
for i in range(N):
    if S[i]=='c':
        print('No')
    elif total>0:
        if S[i] == 'a':
            print('Yes')
            total = total-1
        elif S[i] =='b' and B>0:
            print('Yes')
            total = total-1
            B = B-1
        else:
            print('No')
    else:
        print('No')
