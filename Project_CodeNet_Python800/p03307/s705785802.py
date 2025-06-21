def q1():
    N = int(input())
    d, m = divmod(N,2)
    if m==0:
        ans = N
    else:
        ans = N * 2
    print(ans)


if __name__ == '__main__':
    q1()