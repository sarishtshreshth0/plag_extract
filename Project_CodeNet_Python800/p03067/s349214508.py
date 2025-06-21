def LI():
    return list(map(int, input().split()))


A, B, C = LI()
if A < C < B or B < C < A:
    ans = "Yes"
else:
    ans = "No"
print(ans)
