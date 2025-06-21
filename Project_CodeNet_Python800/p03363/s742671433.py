
from itertools import accumulate
from collections import defaultdict
def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    Acum = [0] + list(accumulate(A))
    dic = defaultdict(int)
    ans = 0
    for i in range(N + 1):
        ans += dic[Acum[i]]
        dic[Acum[i]] += 1

    print(ans)


if __name__ == "__main__":
    resolve()