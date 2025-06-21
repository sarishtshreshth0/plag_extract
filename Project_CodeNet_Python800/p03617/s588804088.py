Q, H, S, D = map(int, input().split())
N =int(input())

p = min([Q*4,H*2,S])

p1 = p*N
p2 = D*(N//2) + p*(N%2)
print(min([p1,p2]))