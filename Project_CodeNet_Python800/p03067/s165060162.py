A,B,C = list(map(int,input().split(' ')))
if C>min(A,B) and C<max(A,B):
    print('Yes')
else:
    print('No')