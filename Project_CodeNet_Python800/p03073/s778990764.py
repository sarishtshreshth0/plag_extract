s = input()
phase = 'Odd'
ptn10 = 0
ptn01 = 0
for i in s:
  if phase == 'Odd':
    if i == '1':
      ptn01 += 1
    else:
      ptn10 += 1
    phase = 'Even'
  else:
    if i == '0':
      ptn01 += 1
    else:
      ptn10 += 1
    phase = 'Odd'
print(min(ptn10, ptn01))