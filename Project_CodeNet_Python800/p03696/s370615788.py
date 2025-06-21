def main():
    N = int(input())
    S = input()
    h_left, h_min, h_cur = 0, 0, 0
    for c in S:
        if c == '(':
            h_cur += 1
        else:
            h_cur -= 1
        h_min = min(h_min, h_cur)
    h_right = h_cur
    if h_min < 0:
        h_left -= h_min
        h_right -= h_min
    print('(' * h_left + S + ')' * h_right)


if __name__ == '__main__':
    main()