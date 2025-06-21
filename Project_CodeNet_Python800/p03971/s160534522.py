N, A, B = map(int, input().split())
S = input()
a = 0
b = 0
ans = "No"
for v, k in enumerate(S, 1):
    if k == "a":
        if a+b < A+B:
            print("Yes")
            a += 1
        else:
            print("No")
    elif k == "b":
        if a+b < A+B and b < B:
            print("Yes")
            b += 1
        else:
            print("No")
    else:
        print("No")