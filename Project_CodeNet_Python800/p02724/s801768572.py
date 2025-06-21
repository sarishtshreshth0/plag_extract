x = int(input())
ans = 0
for a in range(2*10**6):
    if x >= 500:
        x = x-500
        ans = ans + 1000
    else:
        break
for b in range(100):
    if x >= 5:
        x = x-5
        ans = ans + 5
    else:
        break
print(ans)