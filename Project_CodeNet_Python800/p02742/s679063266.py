H, W = [int(i) for i in input().split()]

masu_sum = H * W

if H == 1 or W == 1:
    ans = 1
elif masu_sum % 2 == 0:
    ans = masu_sum // 2
else:
    ans = masu_sum // 2 + 1

print(ans)