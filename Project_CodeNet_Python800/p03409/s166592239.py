def main():
    N = int(input())
    reds = [list(map(int, input().split(' '))) for _ in range(N)]
    blues = [list(map(int, input().split(' '))) for _ in range(N)]
    blues.sort(key=lambda b: b[0])
    used_reds = [0 for _ in range(N)]
    for b in blues:
        candidates = [(i, reds[i]) for i in range(N) \
                      if used_reds[i] == 0 and reds[i][0] < b[0] and reds[i][1] < b[1]]
        if len(candidates) == 0:
            continue
        highest_index, highest_h = None, -1
        for i, r in candidates:
            if r[1] > highest_h:
                highest_h = r[1]
                highest_index = i
        used_reds[highest_index] = 1
    print(sum(used_reds))


if __name__ == '__main__':
    main()
