n = int(input())
list_ = []
flag = 0
for i in range(n):list_.append(input())
if n == len(set(list_)):
        for i in range(n - 1):
            if list_[i][-1] != list_[i+1][0]:
                flag += 1
                break
        if flag == 0:
            print("Yes")
        else:
            print("No")
else:
    print("No")