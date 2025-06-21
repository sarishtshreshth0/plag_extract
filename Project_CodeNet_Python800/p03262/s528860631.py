import math

def solve():
    arr = [0]*N
    ans = abs(start-x[0])
    for i in range(1,N):
        arr[i] = (abs(start-x[i]))
        ans = math.gcd(arr[i], ans)
    print(ans)
        
if __name__=="__main__":
    N,start = list(map(int, input().split()))
    x = list(map(int, input().split()))
    solve()

