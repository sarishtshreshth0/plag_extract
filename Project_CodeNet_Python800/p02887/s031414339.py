N = int(input())
S = input()
ans = [S[0]]
for i in range(1, N):
    if S[i]==ans[-1]:
        continue
    else:
        ans.append(S[i])
print(len(ans))