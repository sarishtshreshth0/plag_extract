N =int(input())

list = [[3,5,7]]

for i in range(9):
    new =[]
    for j in list[-1]:
        new.append(10*j+3)
        new.append(10*j+5)
        new.append(10*j+7)
    list.append(new)

a_list=[]
ans =0
for i in list:
    for j in i:
        if N <j:
            print(ans)
            exit()
        if '3' in str(j) and '5' in str(j) and '7' in str(j):
            ans += 1