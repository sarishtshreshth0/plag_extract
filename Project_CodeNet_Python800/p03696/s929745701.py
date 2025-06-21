N = int(input())
S = input()

L, R = 0, 0
cnt = 0
for s in S:
    if s == '(':
        cnt += 1
    else:
        if cnt > 0:
            cnt -= 1
        else:
            L += 1

R = cnt
print(L * '(' + S + R * ')')