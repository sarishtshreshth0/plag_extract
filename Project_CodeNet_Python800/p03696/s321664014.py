n = int(input())
s = input()

minv = 0
score = 0
for i in range(n):
    if s[i] == '(':
        score += 1
    else:
        score -= 1
    minv = min(minv, score)

ans = ""
for i in range(0, -minv):
    ans += "("
ans += s
for i in range(0, score-minv):
    ans += ")"
print(ans)