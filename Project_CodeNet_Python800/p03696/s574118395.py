import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = LS2()

a,b = 0,0
left = []
for i in range(N):
    if S[i] == '(':
        a += 1
    else:
        b += 1
    if a < b:
        a,b = 0,0
        left.append('(')

ANS = left + S + [')']*(a-b)

print(''.join(ANS))