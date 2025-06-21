N,A,B=map(int,input().split())
S=input()

Pass=0
count=0
for s in S:
    if s=='a' and Pass<A+B:
        Pass+=1
        print('Yes')
    elif s=='b':
        count+=1
        if Pass<A+B and count<B+1:
            Pass+=1
            print('Yes')
        else:
            print('No')
    else:
        print('No')