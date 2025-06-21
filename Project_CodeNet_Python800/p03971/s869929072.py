N,A,B = map(int,input().split())
S = input()

count_in = 0
count_out = 0
for s in S:
    if s == 'a':
        if count_in+count_out<A+B:
            print('Yes')
            count_in += 1
            continue

    if s == 'b':
        if count_out<B and count_in+count_out<A+B:
            print('Yes')
            count_out += 1
            continue
    print('No')

