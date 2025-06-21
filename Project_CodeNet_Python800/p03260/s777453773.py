def resolve():
    inputs = list(map(int, input().split()))
    print("No" if 2 in inputs else "Yes")


if '__main__' == __name__:
    resolve()