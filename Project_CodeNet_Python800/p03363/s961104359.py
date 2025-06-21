n = int(input())
a = list(map(int, input().split()))

cs = [0]*(n+1)
cs[0] = a[0]
for i in range(1, n+1):
    cs[i] += cs[i-1] + a[i-1]
cs.sort()
total = 0
focus = None
count = 0
for s in cs:
    if s == focus:
        count += 1
    else:
        total += count * (count-1)//2
        focus = s
        count = 1
total += count * (count-1)//2
print(total)
