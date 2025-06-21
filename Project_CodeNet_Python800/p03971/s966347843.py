def resolve():
    N, A, B = map(int, input().split())
    S = input()
    count = 1
    sabetu = 1
    for i in range(N):
        if S[i] == "a" and count <= A+B:
            count += 1
            print("Yes")
        elif S[i] == "b" and sabetu <= B and count <= A+B:
            sabetu += 1
            count += 1
            print("Yes")
        else:
            print("No")
resolve()