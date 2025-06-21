S = list(input())
f = False
c = 0

for i  in range(len(S) - 1):
    # if i == len(S) - 2:
    #     break
    if S[i] != S[i + 1]:
        continue
    else:
        if S[i] == "0":
            S[i+1] = "1"
            c += 1
        else:
            S[i+1] = "0"
            c += 1

print(c)