n, a, b = map(int, input().split())
s = input()

passed = 0
foreign = 0
for c in s:
    if c == "a":
        if passed < a + b:
            print("Yes")
            passed += 1
        else: print("No")
    elif c == "b":
        foreign += 1
        if passed < a + b and foreign <= b:
            print("Yes")
            passed += 1
        else: print("No")
    else:
        print("No")