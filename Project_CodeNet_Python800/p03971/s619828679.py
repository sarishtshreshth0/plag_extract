n,a,b = map(int,input().split(" "))
s = input()
m_dict = {"a":0,"b":0,"c":0}
for i in s:
  if i == "a":
    if m_dict["a"]+m_dict["b"] < a+b:
      m_dict["a"] += 1
      print("Yes")
    else:
      print("No")
  elif i == "b":
    if m_dict["a"]+m_dict["b"] < a+b and m_dict["b"] < b:
      m_dict["b"] += 1
      print("Yes")
    else:
      print("No")
  else:
    print("No")