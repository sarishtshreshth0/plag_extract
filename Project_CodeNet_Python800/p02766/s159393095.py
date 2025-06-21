n, k = map(int, input().split(" "))


def calc(n, k):
    r = ""
    while n > 0:
        n, remainder = divmod(n, k)
        r += str(remainder)
    return r[::-1]


print(len(calc(n, k)))