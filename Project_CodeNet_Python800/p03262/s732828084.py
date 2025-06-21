import fractions

def main():
    N, start = map(int, input().split())
    X = list(map(int, input().split()))
    dists = []
    for x in X:
        dists.append(abs(x - start))

    ans = dists[0]
    for d in dists[1:]:
        ans = fractions.gcd(ans, d)
    print(ans)


if __name__ == '__main__':
    main()
