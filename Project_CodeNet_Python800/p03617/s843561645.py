Q,H,S,D = map(int,input().split())
N = int(input())
num = min(4*Q,2*H,S)
if num*2 <= D:
    print(N*num)
elif N % 2 == 0:
    print(N*D//2)
else:
    print(N//2*D+num)