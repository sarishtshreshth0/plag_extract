n = int(input())
w = list()
f = input()
w.append(f)
cnt = 0
for i in range(1, n):
    x = input()
    a = w[i-1]
    if a[-1] == x[0]:
        if x not in w:
            cnt += 1
            w.append(x)
            if cnt == n-1:
                print("Yes")
                break
        else:
            print("No")
            break
    else:
        print("No")
        break