# coding: utf-8

def main():
    N, A, B = map(int, input().split())
    S = input()
    cnt, cnt_f = 0, 0

    for c in S:
        if c == 'c':
            ans = 'No'
        elif c == 'a':
            if A + B > cnt:
                ans = 'Yes'
                cnt += 1
            else:
                ans = 'No'
        else:
            if A + B > cnt and B > cnt_f:
                ans = 'Yes'
                cnt += 1
                cnt_f += 1
            else:
                ans = 'No'
        print(ans)


if __name__ == "__main__":
    main()
