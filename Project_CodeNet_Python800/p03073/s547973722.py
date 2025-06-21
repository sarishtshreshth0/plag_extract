def main():
    S = list(input().rstrip())
    list1, list2 = [], []
    for i in range(len(S)):
        if i % 2 == 0:
            list1.append('1')
            list2.append('0')
        else:
            list1.append('0')
            list2.append('1')
    v1 = sum([1 for e, s in zip(list1, S) if e != s])
    v2 = sum([1 for e, s in zip(list2, S) if e != s])
    print(min([v1, v2]))


if __name__ == '__main__':
    main()
