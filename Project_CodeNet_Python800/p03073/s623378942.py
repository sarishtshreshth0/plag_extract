s = input()
n = len(s)

diff0 = 0
diff1 = 0

for i in range(n):
    m = int(s[i])
    if i % 2 != m:
        diff0 += 1
    else:
        diff1 += 1
print(min(diff0, diff1))
