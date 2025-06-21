def main():
    from itertools import accumulate
    from collections import Counter
    _ = int(input())
    A = [int(i) for i in input().split()]
    S = list(accumulate([0] + A))
    c = Counter(S)
    ans = 0
    for v in c.values():
        ans += v*(v-1)//2
    print(ans)


if __name__ == '__main__':
    main()
