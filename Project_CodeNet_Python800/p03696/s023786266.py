N = int(input())
S = input()

ans = S
cnt = 0
now = ""
for s in S:
    now = s
    if s == "(":
        cnt += 1
    elif s == ")":
        cnt -= 1
    if cnt == -1:
        ans = "(" + ans
        cnt = 0
if cnt > 0:
    ans = ans + ")"*cnt

print(ans)