n = int(input())
L = [input() for i in range(n)]

LL = set(L)
if len(LL) != n:
    print('No')
    exit()
    
for i in range(n-1):
    if L[i][-1] != L[i+1][0]:
        print('No')
        exit()
else:
    print('Yes')