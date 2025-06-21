A, B, C = map(int, input().split())


def main():
    if A < C < B:
        return "Yes"
    elif A > C > B:
        return "Yes"
    else:
        return "No"

print(main())
