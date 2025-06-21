Q, H, S, D = list(map(int, input().split()))
Q *= 8
H *= 4
S *= 2
A = min(Q, H, S, D)
B = int(min(Q, H, S) / 2)
N = int(input())
 
print(int(N//2*A+N%2*B))