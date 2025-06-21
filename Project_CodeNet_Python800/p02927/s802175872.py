m ,d = list(map(int , input().split()))
count = 0

for i in range(m):
  for j in range(d):
    month = i + 1
    days = j + 1
    ten_day = days //  10
    one_day = days - ten_day*10
    
    if one_day >= 2 and ten_day>= 2 and month == ten_day * one_day:
      count += 1
      
print(count)