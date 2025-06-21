def resolve():
    N, K = list(map(int, input().split()))
    cnt = 1
    while N >= K**cnt:
        cnt += 1
    print(cnt)

if '__main__' == __name__:
    resolve()