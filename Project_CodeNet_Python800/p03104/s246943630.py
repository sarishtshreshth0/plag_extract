def f(A, B):
    assert A <= B
    if A % 2 == 0 and B % 2 == 1:
        return ((B - A + 1) // 2) % 2
    if A % 2 == 0 and B % 2 == 0:
        return (((B - A) // 2) % 2) ^ B
    if A % 2 == 1 and B % 2 == 1:
        return A ^ (((B - A) // 2) % 2)
    if A % 2 == 1 and B % 2 == 0:
        return A ^ (((B - A - 1) // 2) % 2) ^ B


def main():
    A, B = list(map(int, input().split(' ')))
    print(f(A, B))


if __name__ == '__main__':
    main()