n=int(input())
list_num = [3, 5, 7]
result=[]
def dfs(val):
  if val > n:
    return

  result.append(val)

  for i in list_num:
    dfs(val*10+i)

dfs(0)
count = 0
for i in result:
  str_num = str(i)

  if str_num.count('3') == 0:
    continue
  if str_num.count('5') == 0:
    continue
  if str_num.count('7') == 0:
    continue
  count += 1

print(count)