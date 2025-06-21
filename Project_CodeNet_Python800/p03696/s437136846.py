n = int(input())
S = input()
"""
)))((()())
-3  -1  
左に何個、右に何個
"""
l = 0
r = 0
prev = ")"

for s in S:
    if prev == ")" and s == ")":
        if r > 0:
            r -= 1
        else:
            l += 1
    elif prev == ")" and s == "(":
        r += 1
    elif prev == "(" and s == ")":
        r -= 1
    elif prev == "(" and s == "(":
        r += 1
    # print(s,l,r)
    prev = s
ans = "("*l + S + ")"*r
# print(l,r)
print(ans)
