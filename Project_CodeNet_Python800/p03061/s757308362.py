
N = int(input())
A = list(map(int, input().split()))
        
    
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while b != 0:
        s = a % b
        a = b
        b = s
    return a

F = [A[0]]
for i in range(1, N):
    F.append(gcd(F[-1], A[i]))
#print(F)

A = A[::-1]
B = [A[0]]
for i in range(1, N):
    B.append(gcd(B[-1], A[i]))
#print(B)

MAX = max(B[-2], F[-2])
for i in range(N-2):
    #print(B[-(3+i)], F[i])
    #print(gcd(B[-(3+i)], F[i]))
    MAX = max(MAX, gcd(B[-(3+i)], F[i]))
    
print(MAX)