S = input()
L = len(S)
SS = ""
cnt = 0

if S[0] == "0":
    while len(SS) < L:
        SS += "0"
        SS += "1"

else:
    while len(SS) < L:
        SS += "1"
        SS += "0"

for i in range(L):
    if S[i] != SS[i]:
        cnt += 1

print(cnt)