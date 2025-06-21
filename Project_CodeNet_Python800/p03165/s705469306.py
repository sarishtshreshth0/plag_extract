

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[i][j] - length of the longest common subsequence
    OPT[i][j] = max(OPT[i-1][j-1]+(1 if s[i] == t[j] else 0),
                    OPT[i-1][j],
                    OPT[i][j-1])
    """
    s = input().strip()
    t = input().strip()
    OPT = [[0]*(len(t)+1) for _ in range(len(s)+1)]
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            OPT[i][j] = max(OPT[i-1][j-1]+(1 if s[i-1] == t[j-1] else 0),
                            OPT[i-1][j],
                            OPT[i][j-1])
    i, j = len(s), len(t)
    ans = []
    while i != 0 and j != 0:
        if OPT[i][j] == OPT[i-1][j]:
            i -= 1
        elif OPT[i][j] == OPT[i][j-1]:
            j -= 1
        else:
            ans.append(s[i-1])
            i -= 1
            j -= 1
    return ''.join(ans[::-1])


if __name__ == '__main__':
    print(solve())
