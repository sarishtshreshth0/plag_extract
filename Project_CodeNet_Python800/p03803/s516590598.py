def solve():
    A, B = map(int, input().split())
    if A == B:
        print('Draw')
    elif A == 1 or (B != 1 and B < A):
        print('Alice')
    else:
        print('Bob')

if __name__ == "__main__":
    solve()