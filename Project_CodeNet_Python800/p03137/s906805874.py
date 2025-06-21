n,m = map(int,input().split())
x_list = list(map(int,input().split()))
x_list.sort()
dif_list = []
for i in range(1,m):
  dif_list.append(x_list[i] - x_list[i-1])
  
dif_list.sort(reverse = True)
if n - 1 >= len(dif_list):
  print(0)
else:
  print(sum(dif_list[n-1:]))