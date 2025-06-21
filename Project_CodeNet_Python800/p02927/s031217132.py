m, d = map(int, input().split())
count = 0
d10, d1 = divmod(d,10)
import sys
if d <= 21:
    print(0)
    sys.exit()
for i in range(2,d10 + 1):
    for j in range(2,10):
        for k in range(1,m+1):
            if i*10+j <= d and j*i == k:
                count += 1
print(count)