A, B, C = map(int, input().split())
if (A - C) * (B - C) < 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)