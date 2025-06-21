N, A, B = map(int, input().split())
S = input()
ps = 0
os_r = 0
for s in S:
    if s == 'c':
        print("No")
    elif s == 'a':
        if ps < A + B:
            print("Yes")
            ps += 1
        else:
            print("No")
    else:
        if ps < A + B and os_r < B:
            print("Yes")
            ps += 1
            os_r += 1
        else:
            print("No")