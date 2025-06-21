s = input()
cnt = 0
for i, ss in enumerate(s):
  if ss == str(i % 2):
    cnt += 1
print(min(cnt, len(s) - cnt))