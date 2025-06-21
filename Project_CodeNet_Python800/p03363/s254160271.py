from itertools import accumulate
from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0, ] + list(accumulate(A))
    c = Counter(B)
    ans = 0
    for k, v in c.items():
            ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()
