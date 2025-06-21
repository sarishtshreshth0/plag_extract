import sys

H, W = map(int, input().split())
if H == 1 or W == 1:
    print(1)
    sys.exit()

a = H * W
if a % 2 == 0:
    answer = a // 2
else:
    answer = a // 2 + 1
print(answer)