N,A,B = map(int, input().split())
li = input()
pl_type = list(li)
tuuka_sum = 0
fore_rank = 1
for i in range(N):
 if pl_type[i] == 'c':
     print('No')
 elif pl_type[i] == 'a' and tuuka_sum < A+B:
     print('Yes')
     tuuka_sum += 1
 elif pl_type[i] == 'b' and tuuka_sum < A+B:
     if fore_rank <= B:
         print('Yes')
         fore_rank += 1
         tuuka_sum += 1
     else:
         print('No')
 else:
     print('No')
