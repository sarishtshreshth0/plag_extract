a, b = map(int, input().split())
flg = False
for c in range(1,4):
    if a*b*c%2 == 1:
        flg = True
        break
print("Yes" if flg else "No")