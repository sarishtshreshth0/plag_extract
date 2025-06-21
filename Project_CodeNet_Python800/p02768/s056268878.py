MOD = pow(10, 9)+7

def combi(n, k, MOD):
    numer = 1
    for i in range(n, n-k, -1):
        numer *= i
        numer %= MOD
    denom = 1
    for j in range(k, 0, -1):
        denom *= j
        denom %= MOD
    return (numer*(pow(denom, MOD-2, MOD)))%MOD

def main():
    n, a, b = map(int, input().split())
    allsum = pow(2, n, MOD)
    s1 = combi(n, a, MOD)
    s2 = combi(n, b, MOD)
    ans = (allsum - s1 - s2 - 1)%MOD
    print(ans)

if __name__ == "__main__":
    main()
