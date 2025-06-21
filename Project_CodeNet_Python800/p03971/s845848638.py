n, a, b = list(map(int, input().split()))

s = str(input())

count_a = 0
count_b = 0

for i in s:
  
  j = ""
  
  if count_a+count_b >= (a+b):
    j = "No"
  
  elif i == "a":
    count_a += 1
    j = "Yes"
    
  elif i=="b":
    j = "Yes"
    
    if count_b >= b:
      j = "No"
    
    else:
      count_b += 1
      
  else:
    j = "No"
    
  print(j)