s = input()
s_list = []
ans = ['Y', 'A', 'K', 'I']
for i in s:
    s_list.append(i)
s_list = s_list[:4]
if s_list == ans:
    print('Yes')
else:
    print('No')
