N,A,B = map(int,input().split())
S = input()

ok = foreign = 0
for c in S:
    if c=='a':
        if ok < A+B:
            ok += 1
            print('Yes')
            continue
    elif c=='b':
        if ok < A+B and foreign < B:
            ok += 1
            foreign += 1
            print('Yes')
            continue
    print('No')