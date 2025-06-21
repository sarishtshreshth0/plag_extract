N, A, B = [int(_) for _ in input().split()]
S = input()

ca, cb = 0, 0
for s in S:
    if s == "a":
        if ca + cb < A + B:
            print("Yes")
            ca += 1
        else:
            print("No")
    elif s == "b":
        if ca + cb < A + B and cb < B:
            print("Yes")
            cb += 1
        else:
            print("No")
    else:
        print("No")
