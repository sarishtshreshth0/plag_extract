h,w = map(int, input().split())
total = h * w

if h == 1 or w == 1:
    print(1)
    exit()

if total % 2:
    ans = (total + 1)//2

else:
    ans = total//2

print(ans)
