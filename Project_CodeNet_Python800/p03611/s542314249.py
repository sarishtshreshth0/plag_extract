import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = LI()

ANS = [0]*(10**5+1)
for i in range(N):
    b = a[i]
    if b == 0:
        ANS[b] += 1
        ANS[b+1] += 1
    else:
        ANS[b-1] += 1
        ANS[b] += 1
        ANS[b+1] += 1
        
print(max(ANS))
