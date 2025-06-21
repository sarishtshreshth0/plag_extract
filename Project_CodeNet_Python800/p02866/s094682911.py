MOD = 998244353

def solve():
    if D[0] != 0 or 0 in D[1:]:
        print(0)
        return

    tree_dict = dict()
    max_dist = 0
    for idx, dist in enumerate(D):
        tree_dict[dist] = tree_dict.get(dist, 0) + 1
        max_dist = max(max_dist, dist)
    ret = 1

    for dist in range(max_dist + 1):
        if not dist in tree_dict:
            print(0)
            return
        ret = (ret * pow(tree_dict.get(dist - 1, 1), tree_dict[dist])) % MOD
    print(ret)

if __name__ == "__main__":
    N = int(input())
    D = list(map(int, input().split()))
    solve()