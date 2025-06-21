def resolve():
    n, a, b = map(int, input().split())
    ss = input()
    b_count = 0
    total = 0
    for i, s in enumerate(ss):
        i += 1
        if s == "a":
            if total < a+b:
                total += 1
                print("Yes")
                continue
        elif s == "b":
            b_count += 1
            if total < a+b and b_count <= b:
                total += 1
                print("Yes")
                continue
        print("No")
resolve()