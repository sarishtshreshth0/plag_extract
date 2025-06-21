if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    count = 0

    for i in range(2,a[0]+1):
        for j in range(2,a[1]+1):
            if j > 9:
                k = str(j)
                if i == int(k[0])*int(k[1]) and int(k[0]) > 1 and int(k[1]) >1:
                    count+=1

    print(count)