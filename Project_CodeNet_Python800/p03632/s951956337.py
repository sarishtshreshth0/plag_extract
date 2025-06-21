A, B, C, D = map(int, input().split())

r = min(B, D) - max(A, C)
if r > 0:
    print(r)
    exit()
print(0)