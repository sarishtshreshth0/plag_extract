from sys import stdin

n = int(stdin.readline().strip())
a_lst = [int(x) for x in stdin.readline().strip().split()]
counter_dict = {}

# create counter dict
for a in a_lst:
  counter_dict[a] = counter_dict.get(a, 0) + 1

# check
max_val = -1
for x in range(min(a_lst), max(a_lst)+1):
  sum_val = counter_dict.get(x-1, 0) + counter_dict.get(x, 0) + counter_dict.get(x+1, 0)
  if sum_val > max_val:
    max_val = sum_val

print(max_val)