from fractions import gcd

def mygcd(x, y):
    if x == 0 or y == 0:
        return max(x, y)
    return gcd(x, y)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    L = [0]; R = [0]
    for i in range(len(A)):
        Lbase = mygcd(L[-1], A[i])
        L.append(Lbase)
        Rbase = mygcd(R[-1], A[-i-1])
        R.append(Rbase)
    
    ans = 0
    R.reverse()
    for i in range(len(A)):
        tmp = mygcd(L[i], R[i+1])
        ans = max(ans, tmp)

    print(ans)

if __name__ == "__main__":
    main()
