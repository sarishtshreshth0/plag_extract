n = int(input())
w = [input()]
for i in range(n-1):
    tmp = input()
    if w[i][-1] == tmp[0]:
        flg = tmp in w
        if flg == False:
            w.append(tmp)
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()
print('Yes')