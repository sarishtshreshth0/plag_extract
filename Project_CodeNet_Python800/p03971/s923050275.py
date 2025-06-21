# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

N, A, B = map(int, input().split())
S = input()

P = 0
Pb = 0
for i in range(len(S)):
    if S[i] == 'a':
        if P < A + B:
            P += 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "b":
        if P < A + B and Pb < B:
            P += 1
            Pb += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
