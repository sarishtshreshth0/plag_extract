import sys

N, K = map(int, input().split())

if K == 10:
    print(len(str(N)))
    sys.exit()

p = 0
while True:
    num = K ** p
    if N < num:
        break
    p += 1

print(p)
