n = int(input())
s = list(input())
ans = "".join(s)

f = True
while f:
    f = False
    l = [True] * len(s)
    ns = []
    for i in range(len(s)-1):
        if (s[i] == "(") and (s[i + 1] == ")"):
            l[i], l[i + 1] = False, False
            f = True

    for i in range(len(s)):
        if l[i]:
            ns.append(s[i])

    s = ns.copy()

cnt = [0, 0]
for c in s:
    cnt[c == "("] += 1

print("(" * cnt[0] + ans + ")" * cnt[1])
