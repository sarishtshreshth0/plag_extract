def resolve():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))
    b = list(accumulate(a))
    from collections import Counter
    c = Counter(b + [0])
    def calc(x): return x * (x - 1) // 2
    ans = 0
    for k, v in c.items():
        ans += calc(v)
    print(ans)


resolve()
