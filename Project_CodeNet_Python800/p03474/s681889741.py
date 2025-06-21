A, B = map(int, input().split())
S = input()

for i in range(A):
    if S[i].isdecimal():
        pass
    else:
        print("No")
        exit()

if S[A] == "-":
    pass
else:
    print("No")
    exit()

for i in range(A + 1, A + B + 1):
    if S[i].isdecimal():
        pass
    else:
        print("No")
        exit()

print("Yes")
