N,A,B=map(int, input().split())
S=input().strip()

total = 0
totalB = 0
for c in S:
    if c == 'a':
        if total < A + B:
            total += 1
            print('Yes')
        else:
            print('No')
    elif c == 'b':
        if total < A + B and totalB < B:
            total += 1
            totalB += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')