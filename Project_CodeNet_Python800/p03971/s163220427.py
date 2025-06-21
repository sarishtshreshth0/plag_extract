n, a, b = map(int, input().split())
S = input()
cnt = 0
cnt2 = 0
for s in S:
    if s == 'a' and cnt < (a + b):
        print('Yes')
        cnt += 1
    elif s == 'b' and cnt < (a + b)and cnt2 < b:
        print('Yes')
        cnt += 1
        cnt2 += 1
    else:
        print('No')
