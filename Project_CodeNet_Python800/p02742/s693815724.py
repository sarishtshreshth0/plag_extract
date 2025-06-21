h,w = map(int,input().split(" "))
field = h*w
if (h*w) % 2 == 0:
  answer = (h*w)//2
else:
  answer = (h*w)//2 + 1
if h == 1:
  answer = 1
elif w == 1:
  answer = 1
print(answer)
