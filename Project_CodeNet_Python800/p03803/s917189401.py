dic={2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 12:11, 13:12, 1:13}
a, b = map(int, input().split())
if dic[a] < dic[b]:
  print('Bob')
elif dic[b] < dic[a]:
  print('Alice')
else:
  print('Draw')