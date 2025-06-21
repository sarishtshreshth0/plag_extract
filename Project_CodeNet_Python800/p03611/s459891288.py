n = int(input())
a = list(map(int,input().split(" ")))

c_dic = {}
for i in a:
    if i not in c_dic:
        c_dic[i] = 1
    else:
        c_dic[i] += 1
    
    if i + 1 not in c_dic:
        c_dic[i + 1] = 1
    else:
        c_dic[i + 1] += 1

    if i - 1 not in c_dic:
        c_dic[i - 1] = 1
    else:
        c_dic[i - 1] += 1

print(max(c_dic.values()))