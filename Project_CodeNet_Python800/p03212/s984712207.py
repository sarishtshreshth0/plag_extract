N = int(input())

count = 0


def calc(n, n3, n5, n7):
    global count
    if n > N:
        return
    if 1 <= n <= N and n3 and n5 and n7:
        count += 1
    calc(10 * n + 3, 1, n5, n7)
    calc(10 * n + 5, n3, 1, n7)
    calc(10 * n + 7, n3, n5, 1)


calc(0, 0, 0, 0)
print(count)
