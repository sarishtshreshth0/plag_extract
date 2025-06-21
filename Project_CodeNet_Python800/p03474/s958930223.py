A,B = map(int,input().split())
S = list(input())
check = [str(i) for i in range(10)]

okFlag = True
for key,val in enumerate(S):
    if key == A:
        if S[key] != '-':
            okFlag = False
        else:
            continue
    elif S[key] not in check:
        okFlag = False

if okFlag:
    print('Yes')
else:
    print('No')