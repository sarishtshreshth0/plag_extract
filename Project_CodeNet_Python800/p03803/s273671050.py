lst = list(map(int,input().split()))

if lst[1] != 1 and lst[0] > lst[1] :
    print('Alice')
elif lst[0] != 1 and lst[0] < lst[1]:
    print('Bob')
elif lst[1] == 1 and lst[0] != 1:
    print('Bob')
elif lst[0] == 1 and lst[1] != 1:
    print('Alice')
else:
  print('Draw')