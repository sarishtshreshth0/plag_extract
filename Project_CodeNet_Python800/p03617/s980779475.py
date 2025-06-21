Q,H,S,D = map(int, input().split())
N = int(input())
a = N//2 * 2
k =  min(a*Q*4, a*H*2, a*S, a*D//2)
if N%2 == 1:
    k += min(Q*4, H*2, S)
print(k)