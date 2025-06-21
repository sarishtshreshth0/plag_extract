n=int(input())
w=list(map(int,input().split()))
s_1=0
s_2=sum(w)
for i in range(n):
  if abs(s_2 - s_1) >= abs(s_2-s_1-2*w[i]):
    s_2 -= w[i]
    s_1 += w[i]
  else:
    break
print(abs(s_2-s_1))