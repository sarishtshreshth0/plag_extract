#C

n, m = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
length = []
if n >= m:
    print(0)
else:
    #長い道ををm-n個取っておく
    for i in range(m - 1):
        length.append(x[i + 1] - x[i])
    length.sort()
    tmp = sum(length[(m - n):])
    print(x[m-1]-x[0] - tmp)
    # print(x[m-1],length)
