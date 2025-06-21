N = int(input())
w = []
w1 = ""
flag = 0
for i in range(N):
  s = input()
  if i == 0:
    w1 = s
    w.append(w1)
  else:
    if s[0] == w[i-1][-1] and s not in w:
      w1 = s
      w.append(w1)
    else:
      flag += 1
      break
print("No") if flag == 1 else print("Yes")