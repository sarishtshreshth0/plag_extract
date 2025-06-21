#010 または 101にするのにかかる変更数を考えればいいということになる
s=str(input())
n=len(s)
c1=0
c2=0
for i in range(n): #奇数のときに１、偶数で０にする場合
  if i%2==0:
    if s[i]=="1":
      c1+=1
  else:
    if s[i]=="0":
      c1+=1
for i in range(n): #奇数のときに１、偶数で０にする場合
  if i%2==0:
    if s[i]=="0":
      c2+=1
  else:
    if s[i]=="1":
      c2+=1
print(min(c1, c2))