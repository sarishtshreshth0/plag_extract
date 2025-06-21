if __name__ == '__main__':
    a = [int(i) for i in input().split()]

    if min(a[3],a[1]) - max(a[0],a[2]) > 0:
        print(min(a[3],a[1]) - max(a[0],a[2]))
    else:
        print(0)



