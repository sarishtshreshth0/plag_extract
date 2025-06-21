A, B, C = map(int, input().split())
if A < C and C < B:
    ans = "Yes"
elif B < C and C < A:
    ans = "Yes"
else:
    ans = "No"
print(ans)
