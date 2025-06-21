N = int(input())
S = input()
l = 0
cnt = 0
for c in S:
    if c == "(":
        cnt += 1
    else:
        if cnt == 0:
            l += 1
        else:
            cnt -= 1
ans = "("*l + S + ")"*cnt
print(ans)
