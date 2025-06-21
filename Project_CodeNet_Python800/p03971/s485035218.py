N, A, B = map(int, input().split())
S = input()

x = A + B
cnt = 0
bcnt = 0
for s in S:
    if cnt >= x:
        print("No")
        continue
    if s == "a":
        cnt += 1
        print("Yes")
    elif s == "b":
        if bcnt < B:
            cnt += 1
            bcnt += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
