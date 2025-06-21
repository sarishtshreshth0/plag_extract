Q, H, S, D = map(int,input().split())
N = int(input())
R = N%2
M = N//2

print(min([Q*8,H*4,S*2,D])*M+min([Q*4,H*2,S])*R)