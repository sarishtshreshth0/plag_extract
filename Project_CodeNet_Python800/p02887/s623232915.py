def run_length(data, init=''):
    length = []
    tmp = init
    cnt = 0
    for c in data:
        if tmp != c:
            length.append(cnt)
            cnt = 0
        tmp = c
        cnt += 1
    length.append(cnt)
    return length


def resolve():
    n = int(input())
    s = input()
    length = run_length(s, '')
    print(len(length) - 1)


if __name__ == "__main__":
    resolve()
