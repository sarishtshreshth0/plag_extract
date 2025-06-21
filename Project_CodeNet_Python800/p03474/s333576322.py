A,B = map(int,input().split())
S = list(input())
if len(S) != A+B+1:
    print('No')
    exit()
for i,s in enumerate(S):
    if i!=A and s != '-':
        continue
    if i==A and s == '-':
        continue
    print('No')
    exit()
print('Yes')