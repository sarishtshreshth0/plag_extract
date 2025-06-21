n = input()
s = input()
count = 0
max_l = 0
max_r = 0

for c in s:
    if c =="(":
        count -= 1
    else:
        count += 1
    max_l = max(max_l, count)
count = 0
for c in s[::-1]:
    if c =="(":
        count += 1
    else:
        count -= 1
    max_r = max(max_r, count)

print("("*max_l + s + ")"*max_r)