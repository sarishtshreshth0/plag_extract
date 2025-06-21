n = int(input())
s = input()

r = 0
l = 0
for i in s:
    if i == "(":
        r += 1
    else:
        if r == 0:
            l += 1
        else:
            r -= 1

else:
    print("("*l + s + ")"*r)