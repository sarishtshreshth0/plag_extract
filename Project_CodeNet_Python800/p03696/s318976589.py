mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = input().rstrip('\n')

    balance = 0
    balance_min = 0
    for s in S:
        if s == "(":
            balance += 1
        else:
            balance -= 1
        balance_min = min(balance_min, balance)
    ans = S
    if balance_min < 0:
        ans = "(" * (balance_min * -1) + S
        balance -= balance_min
    if balance > 0:
        ans += ")" * balance
    print(ans)


if __name__ == '__main__':
    main()
