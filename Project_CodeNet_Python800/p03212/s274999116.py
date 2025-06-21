def count(s, N):
    if s != "" and int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in "357") else 0
    for c in "357":
        ret += count(s + c, N)
    return ret


def resolve():
    N = int(input())
    print(count("", N))


resolve()
