N, A, B = map(int, input().split())
S = str(input())

AB = A + B

count_all = 0
count_abroad = 0
for i in range(N):
    if S[i] == "a" and count_all < AB:
        count_all += 1
        print("Yes")

    elif S[i] == "b" and count_abroad < B and count_all <AB:
        count_all += 1
        count_abroad += 1
        print("Yes")

    else:
        print("No")