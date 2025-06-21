n, a, b = map(int, input().split())
s = input()

passed = 0
limit = a+b
b_rank = 1

ans_list = []
for w in s:
    if w == 'a':
        if passed < limit:
            ans_list.append('Yes')
            passed += 1
        else:
            ans_list.append('No')
    elif w == 'b':
        if passed < limit and b_rank <= b:
            ans_list.append('Yes')
            passed += 1
        else:
            ans_list.append('No')
        b_rank += 1
    else:
        ans_list.append('No')

for i in ans_list:
    print(i)