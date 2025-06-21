#最後がどういう状態になればいいか考えればいい
s=list(input())
s=list(map(int,s))

n=len(s)
check_1=[i%2 for i in range(n)]
check_2=[(i%2+1)%2 for i in range(n)]

cnt_1=0
cnt_2=0
for i in range(n):
  if s[i]!=check_1[i]:
    cnt_1=cnt_1+1
  if s[i]!=check_2[i]:
    cnt_2=cnt_2+1
print(min(cnt_1,cnt_2))
