A, B = map(int, input().split())
S = list(map(str, input().split("-")))
ans = "No"
if A == len(S[0]):
    if B == len(S[1]):
        ans = "Yes"
print(ans)
