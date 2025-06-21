N, A, B = map(int, input().split())
S = list(input())

x = 0 # 予選の通過人数
b = 1 # 海外勢の予選の通過人数

for S in S:
    if S == "a" and x < A + B:
        x += 1
        print("Yes")
    elif S == "b" and x < A + B and b <= B:
        b += 1
        x += 1
        print("Yes")
    else:
        print("No")