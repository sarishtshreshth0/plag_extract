def solve():
    a, b = map(int, input().split())
    print('YNeos'[a*b % 2 == 0::2])

if __name__ == '__main__':
    solve()
