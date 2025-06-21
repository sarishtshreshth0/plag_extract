m,d = map(int,input().split())
count = 0
for month in range(1,m+1):
  for day in range(1,d+1):
    if (day%10) >= 2 and (day//10) >= 2:
      if (day%10)*(day//10) == month:
        #print(month,day)
        count += 1
print(count)
