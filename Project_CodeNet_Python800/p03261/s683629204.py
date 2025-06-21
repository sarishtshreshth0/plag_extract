n = int(input())
ab = [input() for _ in range(n)] #数字1*複数列入力

l = len(set(ab))

if n != l:
    print("No")
    exit()
for i in range(1,n):
    if ab[i-1][-1] == ab[i][0]:
        pass
    else:
        print("No")
        exit()
print("Yes")    