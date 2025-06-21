N, A, B = map(int, input().split())
S = input()
J = ""

a_cnt = 0
b_cnt = 0

for i in range(N):
    if S[i] == "a":
        if a_cnt + b_cnt < A + B:
            J += "Yes\n"
            a_cnt += 1
        else:
            J += "No\n"
    elif S[i] == "b":
        if a_cnt + b_cnt < A + B and b_cnt < B:
            J += "Yes\n"
            b_cnt += 1
        else:
            J += "No\n"
    else:
        J += "No\n"

print(J)