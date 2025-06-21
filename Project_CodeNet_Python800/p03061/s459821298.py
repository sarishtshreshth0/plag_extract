from math import gcd

def main():
    n = int(input())
    a = list(map(int, input().split()))

    forward = [0] * (n+1)
    forward[0] = a[0]
    for i in range(n):
        forward[i+1] = gcd(forward[i], a[i])

    backward = [0] * (n+1)
    backward[n] = a[n-1]
    for i in range(n-1, -1, -1):
        backward[i] = gcd(backward[i+1], a[i])

    ans = max(forward[n-1], backward[1])
    for i in range(1, n-1):
        candidate = gcd(forward[i], backward[i+1])
        if ans < candidate:
            ans = candidate

    print(ans)

main()