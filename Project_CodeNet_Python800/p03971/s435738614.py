N, A, B = input().split()
A = int(A)
B = int(B)
s = input()

accepted = 0
B_checked = 0

for i in range(len(s)):
    if s[i] == "c":
        print("No")
    elif s[i] == "a":
        accepted += 1
        print("Yes")
    else:
        B_checked += 1
        if (B_checked <= B):
            accepted += 1
            print("Yes")
        else:
            print("No")

    if (accepted >= (A + B)):
        for i in range(len(s) - i - 1):
            print("No")

        break