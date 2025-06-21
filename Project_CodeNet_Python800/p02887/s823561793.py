

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    S = input()
    count = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            count += 1
    return count


if __name__ == '__main__':
    print(solve())
