N = int(input())
if N == 1:
    print(2)
    exit()
ans = N if N % 2 == 0 else 2 * N
print(ans)
