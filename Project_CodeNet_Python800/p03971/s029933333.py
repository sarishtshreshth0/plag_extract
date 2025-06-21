n,a,b = map(int,input().split())
passed=0
out = 0
for i in input():
    if i == "a":
        if passed < a+b:
            passed += 1
            print("Yes")
        else:
            print("No")
    elif i == "b":
        if passed < a+b and out < b:
            passed += 1
            out += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")