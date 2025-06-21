N = int(input())
S = input().strip()
S1 = S
cur = 0
for i in range(len(S)):
    if S[i]=="(":
        cur += 1
    else:
        cur -= 1
    if cur<0:
        S1 = "("+S1
        cur += 1
S1 = S1+")"*cur
print(S1)