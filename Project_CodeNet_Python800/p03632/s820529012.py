A, B, C, D = map(int, input().split())

start = max(A, C)
end = min(B, D)

if start <= end:
    print(end - start)
else:
    print(0)
