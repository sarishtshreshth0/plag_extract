

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    0.25 0.5 1 2
    Q H S D
    N
    """
    Q, H, S, D = read_ints()
    N = read_int()
    min_cost_per_liter = min(4*Q, 2*H, S)
    return min(N*min_cost_per_liter, (N//2)*D+(N%2)*min_cost_per_liter)


if __name__ == '__main__':
    print(solve())
