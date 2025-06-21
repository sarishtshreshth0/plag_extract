N, A, B = map(int, input().strip().split(" "))
students = list(input().strip())

kaigai = 0
total = 0
for s in students:
    if s == "a":
        if total < A+B:
            print("Yes")
            total += 1
        else:
            print("No")
    elif s == "b":
        if total < A+B and kaigai < B:
            print("Yes")
            kaigai += 1
            total += 1
        else:
            print("No")
    else:
        print("No")