A, B = map(int, input().split())
for C in range(4):
    if A * B % 2 != 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()