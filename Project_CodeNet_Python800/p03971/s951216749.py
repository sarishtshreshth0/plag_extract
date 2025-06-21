N, A, B = map(int, input().split())
S = input()
cnt1, cnt2 = 0, 1

for Si in S:
    if Si=='a' and cnt1<A+B:
        print('Yes')
        cnt1 += 1
    elif Si=='b' and cnt1<A+B and cnt2<=B:
        print('Yes')
        cnt1 += 1
        cnt2 += 1
    else:
        print('No')