def main():
    A, B = map(int, input().split())
    if A == B:
        print('Draw')
    elif A == 1 and B <= 13:
        print('Alice')
    elif B == 1 and A <= 13:
        print('Bob')
    elif A > B:
        print('Alice')
    elif B > A:
        print('Bob')
main()