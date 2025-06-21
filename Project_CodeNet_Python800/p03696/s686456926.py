N=int(input())
S=input()
d = [0]*(N+1) # d[i]: Sの最初のi文字における
              # "(" - ")"
for i in range(1, N+1):
    d[i] = S[:i].count("(") - S[:i].count(")")
x = min(d)
# x = 0 かつ d[N]=0ならよい
if x == 0 and d[N] == 0:
    print(S)
    exit()

ans = "("*abs(x) + S + ")"*(d[N]+abs(x))
print(ans)