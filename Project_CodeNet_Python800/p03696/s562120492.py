n = int(input())
s = input()
l, r = 0, 0
for i in s:
    if i == "(":
        r += 1
    elif r > 0 and i == ")":
        r -= 1
    else:
        l += 1

print("(" * l + s + ")" * r)
