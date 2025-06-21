def solve():
    n = int(input())
    h =[]
    for i in range(n):
        w = input()
        if i == 0:
            h.append(w)
            continue
        if w in h:
            print('No')
            exit()
        if h[i-1][-1] != w[0]:
            print('No')
            exit()
        h.append(w)
    print('Yes')


if __name__ == '__main__':
    solve()
