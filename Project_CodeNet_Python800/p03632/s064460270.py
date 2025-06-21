def resolve():
    A, B, C, D = map(int, input().split())
    count = 0
    for i in range(101):
        if A<i<=B and C<i<=D:
            count += 1
    print(count)
resolve()