A, B = map(int, input().split())
S = input()
if S.count("-") != 1:
    print("No")
elif S.index("-") != A:
    print("No")
else:
    print("Yes")