def calc_time_to_next_station(t, c, s, i):
  if t <= s:
    return s + c
  else:
    f = lambda x, y: (x + y - 1) // y
    return f(t-s, i) * i + s + c  


def calc_needed_time(i, cost, start, interval):
  """
  calculate the needed time to reach n-th station when we are at i-th station 
  Args:
    i (int): 0-indexed number
    cost (list)
    start (list)
    interval (list)
  """
  if i == n - 1:
    return 0
  m = len(start)
  t = 0
  for j in range(i, m):
    t = calc_time_to_next_station(t, cost[j], start[j], interval[j])
  return t
 



n = int(input())
cost, start, interval = [], [], []
for _ in range(n-1):
  c, s, i = map(int, input().split())
  cost.append(c)
  start.append(s)
  interval.append(i)


for i in range(n):
  print(calc_needed_time(i, cost, start, interval))
