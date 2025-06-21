N = int(input())
s = input()
def f(s):
    d = 0
    for i in range(len(s)):
        if s[i] == "(":
            d += 1
        else:
            d -= 1
        if d < 0:
            return "("+s
    if d > 0:
        return s+")"
    else:
        print(s)
        exit(0)
while True:
    s = f(s)