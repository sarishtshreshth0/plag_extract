def main():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    for i in range(N):
        x[i] = abs(x[i]-X)
    from math import gcd
    g = x[0]
    for i in range(1,N):
        g = gcd(g,x[i])
    print(g)
main()