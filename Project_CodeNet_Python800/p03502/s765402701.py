def actual(N):
    f = lambda x: sum(map(int, str(N)))

    if N % f(N) == 0:
        return 'Yes'

    return 'No'


N = int(input())
print(actual(N))