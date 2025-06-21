A, B = map(int, input().split())
S = input()

if S[:A].isdecimal() and S[A] == "-" and S[-B:].isdecimal():
    print("Yes")
else:
    print("No")
