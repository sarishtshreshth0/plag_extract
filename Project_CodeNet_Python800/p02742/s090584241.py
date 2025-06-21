H, W = map(int, input().split())
total = H*W
if H == 1 or W == 1:
    ans = 1
elif total % 2 == 0:
    ans = total//2
else:
    total += 1
    ans = total//2
print(ans)
