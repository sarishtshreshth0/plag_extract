def resolve():
    A, B = map(int, input().split())
    S = input()
    C = "1234567890"
    for i in range(A):
        if S[i] in C:
            continue
        else:
            print("No")
            exit()
    if S[A] != "-":
        print("No")
        exit()
    for i in range(A+1, len(S)):
        if S[i] in C:
            continue
        else:
            print("No")
            exit()
    print("Yes")
resolve()