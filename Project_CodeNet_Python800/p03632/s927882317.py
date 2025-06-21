s = input().split()

a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

answer = 0

lower = max(a, c)
upper = min(b, d)

answer = max(0, upper - lower)

print(answer)