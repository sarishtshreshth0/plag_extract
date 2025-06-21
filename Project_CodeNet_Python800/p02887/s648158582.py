n=input()
s = input()
cnt=0
s_list = [word for word in s]

tmp = s_list.pop()
for _ in range(len(s_list)):
  tmp_2 = s_list.pop()
  if tmp!=tmp_2:
    cnt+=1
  tmp=tmp_2
print(cnt+1)