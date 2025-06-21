N, A, B = [int(x) for x in input().split()]
S = input()

rank = 0
foreign_rank = 0
for i in S:
    if i == 'a':
        if rank < A + B:
            rank += 1
            print('Yes')
            continue

    if i == 'b':
        if rank < A + B and foreign_rank < B:
            rank += 1
            foreign_rank += 1
            print('Yes')
            continue

    print('No')
