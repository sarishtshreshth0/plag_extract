lst = [14 if x == 1 else x for x in map(int,input().split())]
if lst[1] != 1 and lst[0] > lst[1] :
    print('Alice')
elif lst[0] != 1 and lst[0] < lst[1]:
    print('Bob')
else:
  print('Draw')
 