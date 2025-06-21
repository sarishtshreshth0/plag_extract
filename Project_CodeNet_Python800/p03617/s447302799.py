Q,H,S,D = map(int, input().split())
N = int(input())
if N >=2:
    if N%2 == 0:
        ans = N//2*min([8*Q,4*H,2*S,D])
    else:
        ans = (N-1)//2*min([8*Q,4*H,2*S,D]) + min([4*Q,2*H,S])
else:
    ans = min([4*Q,2*H,S])
print(ans)