from math import sqrt, floor
N = int(input())

# 素因数分解

left = []
right = []
for i in range(1, floor(sqrt(N)) + 1):
    if (N % i == 0):
        left.append(i)
        right.append(N // i)
    else:
        continue

last_left = str(left[-1])
last_right = str(right[-1])

ans = []
for i in range(len(left) - 1, -1, -1):
    ans.append(max(len(str(left[i])), len(str(right[i]))))

print(min(ans))
