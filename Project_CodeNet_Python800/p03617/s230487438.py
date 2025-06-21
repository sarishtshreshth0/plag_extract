Q,H,S,D = list(map(int,input().split()))
N = int(input())*100
TL = sorted([(25,Q,8*Q),(50,H,4*H),(100,S,2*S),(200,D,D)],key=lambda x: x[2])
ans = 0
if N >= TL[0][0]:
    ans += (N//TL[0][0])*TL[0][1]
    N %= TL[0][0]
if N >= TL[1][0]:
    ans += (N//TL[1][0])*TL[1][1]
    N %= TL[1][0]
if N >= TL[2][0]:
    ans += (N//TL[2][0])*TL[2][1]
    N %= TL[2][0]
if N >= TL[3][0]:
    ans += (N//TL[3][0])*TL[3][1]
    N %= TL[3][0]
print(ans)