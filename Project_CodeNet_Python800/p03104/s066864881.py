if __name__ == '__main__':
    def judge(x):
        if x % 4 == 0:
            return x
        elif x % 4 == 1:
            return 1
        elif x % 4 == 2:
            return x + 1
        else:
            return 0

    a, b = map(int, input().split())
    fa = judge(a - 1)
    fb = judge(b)
    print(fa ^ fb)
