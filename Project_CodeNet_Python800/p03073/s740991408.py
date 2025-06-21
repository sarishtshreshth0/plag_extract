
S = input()

ctr = [0, 0]
for i in range(len(S)):
    if i % 2 == 0:
        ctr[0] += int(S[i]) == 0
        ctr[1] += int(S[i]) == 1
    else:
        ctr[0] += int(S[i]) == 1
        ctr[1] += int(S[i]) == 0

print(min(ctr))
