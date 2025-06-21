N = int(input())
S = list(input())
S.append("test")
i = 0
while N > 0:
    if S[i] == S[i+1]:
        S.pop(i)
        i = i - 1
    i = i + 1
    N = N - 1
print(len(S)-1)
