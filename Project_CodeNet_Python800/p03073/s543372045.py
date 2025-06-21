S = input()
length = len(S)
p1 = [0 if i % 2 == 0 else 1 for i in range(length)]
p2 = [1 if i % 2 == 0 else 0 for i in range(length)]
ans1 = 0
ans2 = 0
for index,s in enumerate(S):
  if int(s) != p1[index]:
    ans1 += 1
  if int(s) != p2[index]:
    ans2 += 1
  
print(min(ans1,ans2))