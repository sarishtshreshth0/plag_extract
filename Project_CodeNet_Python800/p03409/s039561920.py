import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    red = []
    for _ in range(N):
        a, b = map(int, input().split())
        red.append((a, b))
    red_fin = set()
    blue = []
    for _ in range(N):
        c, d = map(int, input().split())
        blue.append((c, d))
    blue.sort()

    """
    解説pdfの通り、x方向に見た上で青い点に対応する赤い点の最適な物を貪欲に選べば良い。
    これが最適であることの証明は、非最適なペアリングを上述のペアリングに「「１組」」繋ぎ直しても
    ペアの個数が減らないことを見れば良い。
    （x+yが小さい順に見ればいけるかなと想定したのが外れルート。。。）
    """

    ans = 0
    for c, d in blue:
        cand = (-1, -1)
        for a, b in red:
            if a < c and b < d and cand[1] < b and (a, b) not in red_fin:
                cand = (a, b)
        if cand == (-1, -1): continue
        ans += 1
        red_fin.add(cand)
    print(ans)





if __name__ == "__main__":
    main()
