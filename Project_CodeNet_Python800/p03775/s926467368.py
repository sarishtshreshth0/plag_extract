from math import sqrt
def solve():
    N = int(input())
    ans = float('inf')
    for A in range(1,int(sqrt(N))+1):
        if N % A == 0:
            ans = min(ans, len(str(N//A)))
    
    print(ans)

if __name__ == '__main__':
    solve()