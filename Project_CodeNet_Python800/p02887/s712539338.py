N = int(input())
S = input()

for i in range(N - 1):
    if S[i] == S[i + 1]:
        S = S[:i] + '_' + S[i + 1:]

print(len(S.replace('_', '')))
