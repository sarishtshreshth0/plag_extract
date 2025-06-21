n, a, b = map(int, input().split())
s = input()
a_n = 0
b_n = 0
for i in range(len(s)):
  m = s[i:i+1]
  if(m == "a"):
    if(a_n + b_n < a + b):
      print("Yes")
      a_n += 1
    else:
      print("No")
  elif(m == "b"):
    if((a_n + b_n < a + b) and (b_n < b)):
      print("Yes")
      b_n += 1
    else:
      print("No")
  else:
    print("No")