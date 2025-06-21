import collections

class common_function():
    """
        1. よく使いそうで予め用意してあるものをまとめた
        2. よく使いそうな関数群をまとめた
    """
    def nCk(self, n:int, k:int):
        """
            mod を使用しない combination nCk を求めるメソッド
            1回 の nCk を求めるのに O(k) かかる.
        """
        k = min(k, n-k)
        numer = 1
        for i in range(n, n-k, -1):
            numer *= i
        denom = 1
        for i in range(k, 1, -1):
            denom *= i
        return numer // denom

def main():
    common = common_function()
    N = int(input())
    A = list(map(int, input().split()))
    cum = [0]
    for a in A:
        tmp = cum[-1] + a
        cum.append(tmp)
    cumcount = list(collections.Counter(cum).items())
    cumcount.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for number, count in cumcount:
        if count <= 1:
            break
        ans += common.nCk(count, 2)
    print(ans)

if __name__ == "__main__":
    main()
