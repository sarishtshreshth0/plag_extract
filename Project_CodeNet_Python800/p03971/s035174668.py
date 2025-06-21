N, A, B = map(int, input().split())
S = list(input())

passed = 0
foreign = 0

for i, s in enumerate(S):
    if s == "a" and passed < A + B:
        print("Yes")
        passed += 1
    elif s == "b":
        foreign += 1
        if passed < A + B and foreign <= B:
            print("Yes")
            passed += 1
        else:
            print("No")
    else:
        print("No")
