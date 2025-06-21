A, B = map(int, input().split())
def f(x):
    chk = x % 4
    if chk == 0:
        return x
    if chk == 1:
        return 1
    if chk == 2:
        return x + 1
    if chk == 3:
        return 0

if A != 0:
    A -= 1
print(f(A) ^ f(B))