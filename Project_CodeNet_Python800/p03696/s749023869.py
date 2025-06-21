n = int(input())
s = input()
dist = 0
mlow = 0
for i in s:
    if i == ")":
        dist -= 1
        if dist < mlow:
            mlow = dist
    else:
        dist += 1

left = "("*(-mlow)
right = ")"*(dist-mlow)
print(left+s+right)
