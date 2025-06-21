N = int(input())
S = input()

l = 0
r = 0
for i in range(N):
    if S[i]==")":
        r -= 1
        if r<0:
            l += 1
            r = 0
    else:
        r += 1

ans = "("*l + S + ")"*r

print(ans)