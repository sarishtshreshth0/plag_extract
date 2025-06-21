N = int(input())
S = input()

ans = []
for i in range(len(S)):
    if i == len(S) - 1:
        ans.append(S[i])
        break
    if S[i] != S[i+1]:
        ans.append(S[i])
print(len(ans))