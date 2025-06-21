n, a, b = map(int, input().split())
S = input()

cnt = 0
oversea = 1
for s in S:
    #print(s)
    if s == "a":
        if cnt < a+b:
            print("Yes")
            cnt += 1
        else:
            print("No")
    if s == "b":
        if cnt < a+b and oversea <= b:
            print("Yes")
            cnt += 1
            oversea += 1
        else:
            print("No")
    if s == "c":
        print("No")