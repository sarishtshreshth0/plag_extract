def actual(A, B):
    if A == B:
        return 'Draw'

    if A == 1:
        return 'Alice'

    if B == 1:
        return 'Bob'

    if A > B:
        return 'Alice'
    else:
        return 'Bob'

A, B = map(int, input().split())
print(actual(A, B))