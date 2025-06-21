def solve():
    N = int(input())
    R = [[int(x) for x in input().split()] for i in range(N)]
    B = [[int(x) for x in input().split()] for i in range(N)]
    B.sort()
    selected = set()
    for b in B:
        r_lst = []
        for i in range(len(R)):
            if i in selected: continue
            r = R[i]
            if r[0] < b[0] and r[1] < b[1]:
                r_lst.append(i)
        if len(r_lst) == 0:
            continue
        rym = -1
        rym_i = -1
        for i in r_lst:
            if rym < R[i][1]:
                rym = R[i][1]
                rym_i = i
        selected.add(rym_i)
    return len(selected)
if __name__ == '__main__':
    print(solve())
