# 2020/05/06
# AtCoder Beginner Contest 064 - D

# Input
n = int(input())
s = list(input())
nestlv = 0
nestmax = 0
nestmin = 0
lcnt = 0
rcnt = 0

for i in range(n):
    if s[i] == '(':
        nestlv = nestlv + 1
        nestmax = max(nestmax, nestlv)
    elif s[i] == ')':
        nestlv = nestlv - 1
        nestmin = min(nestmin, nestlv)

ans = ''.join(s)
for i in range(nestmin*(-1)):
    ans = '(' + ans

nestlv = nestlv - nestmin
if nestlv > 0:
    for i in range(nestlv):
        ans = ans + ')'

# Output
print(ans)
