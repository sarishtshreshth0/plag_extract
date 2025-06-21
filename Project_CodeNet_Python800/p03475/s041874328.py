import math
N = int(input())
list_time = []
for i in range(N- 1):
  list_time.append(tuple(map(int, input().split())))
  
"""
駅iを時刻tに発ったとき，駅i+1に到着するのはt+ list_time[i- 1][0]
駅i+1を発つのはt+ list_time[i- 1][0]<= list_time[i][1]+ k* list_time[i][2] となる最小の
k，すなわち
k = max(0, math.ceil((t+ list_time[i- 1][0]- list_time[i][1])/ list_time[i][2]))
について時刻list_time[i][1]+ k* list_time[i][2]
"""

def lastdeparturetime(i, t):
  if(i == N- 1):
    return t
  else:
    k = max(0, math.ceil((t+ list_time[i- 1][0]- list_time[i][1])/ list_time[i][2]))
    T = list_time[i][1]+ k* list_time[i][2]
    return lastdeparturetime(i+ 1, T)
  
for i in range(1, N):
  arrivaltime = lastdeparturetime(i, list_time[i- 1][1])+ list_time[N- 2][0]
  print(arrivaltime)
  
print(0)
