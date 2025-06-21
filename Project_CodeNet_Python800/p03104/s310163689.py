import sys
def input(): return sys.stdin.readline().strip()

def f(a):
    """
    (0 ^ 1 ^ 2 ^ ... ^ a)を返す関数。
    各ビットにおける1の個数をカウントしなくても、
            (2k) ^ (2k+1) = 0
    であることを使えばO(1)で求まる。例えば
    0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 = (0 ^ 1) ^ (2 ^ 3) ^ (4 ^ 5) ^ 6
                              =    1    ^    1    ^    1    ^ 6
                              =    1    ^    6
    """
    if a % 4 == 3: return 0
    if a % 4 == 1: return 1
    if a % 4 == 2: return 1 ^ a
    if a % 4 == 0: return a


def main():
    A, B = map(int, input().split())
    print(f(A - 1) ^ f(B))


if __name__ == "__main__":
    main()
