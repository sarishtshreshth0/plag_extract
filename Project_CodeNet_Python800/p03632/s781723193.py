A, B, C, D = map(int, input().split())
if A >= C:
    start = A
else:
    start = C
if B >= D:
    end = D
else:
    end = B
if end - start <= 0:
    print(0)
else:
    print(end - start)
