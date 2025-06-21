N, A, B = map(int, input().split())
S = input()

a_cnt = 0
b_cnt = 0

for i in range(N):
    if S[i] == "a":
        if a_cnt + b_cnt < A + B:
            print("Yes")
            a_cnt += 1
        else:
            print("No")
    elif S[i] == "b":
        if a_cnt + b_cnt < A + B and b_cnt < B:
            print("Yes")
            b_cnt += 1
        else:
            print("No")
    else:
        print("No")