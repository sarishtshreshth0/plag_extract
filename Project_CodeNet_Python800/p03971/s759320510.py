N, A, B = map(int, input().split())
L = [0, 0]
S = input()

for i in S:
    if i == "a":
        if sum(L) < A + B:
            print("Yes")
            L[0] += 1
        else:
            print("No")
    elif i == "b":
        if sum(L) < A + B and L[1] < B:
            print("Yes")
            L[1] += 1
        else:
            print("No")
    else:
        print("No")
