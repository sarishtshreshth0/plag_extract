A, B, C, D = map(int, input().split())
ans = -1
for i in range(101):
    if (A <= i) and (C <= i) and (i <= B) and (i <= D):
        ans += 1
print(max(ans,0))
