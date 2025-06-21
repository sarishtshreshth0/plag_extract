N = int(input())

S = input()

ans = []

for i in range(N):
    p = S[i]

    if i != N - 1:
        if p != S[i+1]:
            ans.append(S[i])
        else:
            continue
    else:
        ans.append(S[i])

print(len(ans))
