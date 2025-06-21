A,B,C = (int(i) for i in input().split())

if (A < C and C < B) or (B < C and C < A):
    print('Yes')
    
else:
    print('No')