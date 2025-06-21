n = int(input())
S = input()
distinct = 1
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        distinct += 1
print(distinct)