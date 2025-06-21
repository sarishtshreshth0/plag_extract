import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B = mapint()

def cal(N):
    bits = [0]*50
    for i in range(1, 50):
        b = 2**i
        bits[i-1] = ((N//b*(b//2))+max(0, N%b-b//2))
    return bits

a_bits = cal(A)
b_bits = cal(B+1)
ans = 0
for i, (a, b) in enumerate(zip(a_bits, b_bits)):
    ans += 2**i*((a+b)%2)
print(ans)