s = input()
b = 0
w = 0
for i in range(len(s)):
  if s[i] == '0':
    if i % 2 == 0:
      # 偶数番目が0
      w += 1
    else:
      # 奇数番目が0
      b += 1
  else:
    if i % 2 == 0:
      # 偶数番目が1
      b += 1
    else:
      # 奇数番目が1
      w += 1
print(min(b, w))