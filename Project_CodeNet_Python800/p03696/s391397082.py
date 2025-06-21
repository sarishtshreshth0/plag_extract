N = int(input())
S = input().strip()
while True:
    lv = 0
    lmin = len(S)
    for i in range(len(S)):
        if S[i]=="(":
            lv += 1
        else:
            lv -= 1
        lmin = min(lmin,lv)
    if lmin<0:
        S = "("*(-lmin)+S
    else:break
lv = 0
for i in range(len(S)):
    if S[i]=="(":
        lv += 1
    else:
        lv -= 1

if lv>0:
    S = S+")"*lv
print(S)