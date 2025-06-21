n = int(input())
S = input()
ls = [S[0]]
for s in S[1:]:
    if ls[-1] == s:
        continue
    ls.append(s)
print(len(ls))