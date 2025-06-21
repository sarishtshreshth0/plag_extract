a, b = [int(w) for w in input().split()]
s = input()

cond = True

if not s[:a].isnumeric():
    cond = False

if not s[a] == "-":
    cond = False

if not s[a+1:].isnumeric():
    cond = False

print("Yes" if cond else "No")
