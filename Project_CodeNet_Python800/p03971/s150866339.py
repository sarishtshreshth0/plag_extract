x = list(map(int, input().split()))
n = x[0]
a = x[1]
b = x[2]
s = input()


count_domestic = 0
count_oversea = 0
judge_list = []
yes = 'Yes'
no = 'No'

for i in range(n):
    candidate = s[i]
    if candidate == 'a':
        if count_domestic + count_oversea < a + b:
            judge_list.append(yes)
            count_domestic += 1
        else:
            judge_list.append(no)
    elif candidate == 'b':
        if count_domestic + count_oversea < a + b and count_oversea < b:
            judge_list.append(yes)
            count_oversea += 1
        else:
            judge_list.append(no)
    else:
        judge_list.append(no)

for j in range(len(judge_list)):
    print(judge_list[j])
