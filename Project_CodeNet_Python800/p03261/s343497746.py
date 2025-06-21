n=int(input())
e=''
S=[input() for  _ in range(n)]

for w in S:
    if e!=w[0] and e!='':
        print('No')
        exit()
    e=w[-1]

if len(set(S))==n:
    print('Yes')
else:
    print('No')
