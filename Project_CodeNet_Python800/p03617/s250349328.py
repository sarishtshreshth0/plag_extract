if __name__ == "__main__":
    q, h, s, d = map(int, input().split())
    n = int(input())

    # まず1リットルあたりの単価を求める
    value = list()
    value.append(q*4)
    value.append(h*2)
    value.append(s)
    value.append(d/2)

    ans = 0
    if min(value) == value[3]:
        if n % 2 == 1:
            ans += n // 2 * d
            ans += min(value[0:3])
        else:
            ans += n // 2 * d
    else:
        ans += min(value) * n

    print(ans)