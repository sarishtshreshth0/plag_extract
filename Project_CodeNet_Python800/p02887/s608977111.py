
N = int(input())
S = input()

ans = []
a = ""
for i, s in enumerate(S):
    if a != S[i]:
        ans.append(S[i])
        a = S[i]

print(len(ans))