N = int(input())
S = input()

L = 0
R = 0
cnt = 0
d = []
for s in S:
    if s == "(":
       cnt += 1
    else:
        cnt -= 1
        if cnt < 0:
            cnt = 0
            L += 1

R += cnt

print(L*"(" + S + R*")")
