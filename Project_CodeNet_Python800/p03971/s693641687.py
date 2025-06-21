N, A, B = map(int, input().split())
S = input()
participants = 0
i = 1
for s in S:
    if s == 'c':
        print('No')
        continue
    elif s == 'a':
        if participants < A+B:
            print('Yes')
            participants += 1
        else:
            print('No')
    elif s == 'b':
        if participants < A+B and i <= B:
            print('Yes')
            participants += 1
        else:
            print('No')
        i += 1
    

