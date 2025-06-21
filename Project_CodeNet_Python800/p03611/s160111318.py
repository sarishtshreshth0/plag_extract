def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * 10 ** 5
    for i in A:
        if i > 1:
            count[i - 1] += 1
        count[i] += 1
        if i < 10**5-1:
            count[i + 1] += 1
    print(max(count))
resolve()