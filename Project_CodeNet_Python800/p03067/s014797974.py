l = list(map(int, input().split()))
C = l[2]
l.sort()

if l[1] == C:
    print('Yes')
else:
    print('No')
